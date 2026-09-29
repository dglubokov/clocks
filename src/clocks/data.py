"""Downloading and parsing public data (GEO, journal supplements)."""

from __future__ import annotations

import gzip
import io
from pathlib import Path

import pandas as pd
import requests
from tqdm.auto import tqdm

from clocks.paths import DATA_DIR

GEO_FTP = "https://ftp.ncbi.nlm.nih.gov/geo/series"


def download(url: str, dest: Path, *, force: bool = False) -> Path:
    """Download ``url`` to ``dest`` once; later calls return the cached file."""
    dest = Path(dest)
    if dest.exists() and not force:
        return dest
    dest.parent.mkdir(parents=True, exist_ok=True)
    tmp = dest.with_suffix(dest.suffix + ".part")
    with requests.get(url, stream=True, timeout=60, headers={"User-Agent": "Mozilla/5.0"}) as r:
        r.raise_for_status()
        total = int(r.headers.get("content-length", 0)) or None
        bar = tqdm(total=total, unit="B", unit_scale=True, desc=dest.name)
        with open(tmp, "wb") as f, bar:
            for chunk in r.iter_content(chunk_size=1 << 20):
                f.write(chunk)
                bar.update(len(chunk))
    tmp.rename(dest)
    return dest


def geo_url(gse: str, filename: str, kind: str = "matrix") -> str:
    """URL of a file in a GEO series folder (``kind`` is ``matrix`` or ``suppl``)."""
    stub = gse[:-3] + "nnn"
    return f"{GEO_FTP}/{stub}/{gse}/{kind}/{filename}"


def fetch_geo_series_matrix(gse: str) -> Path:
    """Download ``<GSE>_series_matrix.txt.gz`` into ``data/GEO/<GSE>/``."""
    name = f"{gse}_series_matrix.txt.gz"
    return download(geo_url(gse, name), DATA_DIR / "GEO" / gse / name)


def read_geo_series_matrix(path: Path) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Parse a GEO series matrix into ``(samples, values)``.

    ``samples``: one row per GSM with every ``!Sample_*`` field. Repeated
    ``characteristics_ch1`` lines of the form ``key: value`` become their own
    columns (``age``, ``pair id number``, ...).

    ``values``: probes x samples table (for methylation arrays, beta values).
    """
    opener = gzip.open if str(path).endswith(".gz") else open
    with opener(path, "rt", encoding="utf-8", errors="replace") as f:
        lines = f.read().splitlines()

    start = lines.index("!series_matrix_table_begin")
    end = lines.index("!series_matrix_table_end")

    fields: dict[str, list[str]] = {}
    for line in lines[:start]:
        if not line.startswith("!Sample_"):
            continue
        key, *vals = line.split("\t")
        vals = [v.strip('"') for v in vals]
        key = key.removeprefix("!Sample_")
        subkeys = {v.split(": ", 1)[0] for v in vals if v}
        if (
            key.startswith("characteristics_ch")
            and len(subkeys) == 1
            and all(": " in v for v in vals if v)
            and (sub := subkeys.pop()) not in fields
        ):
            # Uniform "key: value" line -> named column. Mixed keys stay raw.
            fields[sub] = [v.split(": ", 1)[1] if v else None for v in vals]
        else:
            n = sum(k == key or k.startswith(key + ".") for k in fields)
            fields[key if n == 0 else f"{key}.{n}"] = vals

    samples = pd.DataFrame(fields).set_index("geo_accession")
    values = pd.read_csv(io.StringIO("\n".join(lines[start + 1 : end])), sep="\t", index_col=0)
    values.columns = values.columns.str.strip('"')
    values.index = values.index.str.strip('"')
    return samples, values
