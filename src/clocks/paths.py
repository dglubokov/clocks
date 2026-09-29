"""Project paths. Data is cached under ``<repo>/data`` (gitignored).

Set the ``CLOCKS_DATA_DIR`` environment variable to keep the cache elsewhere,
e.g. on a larger disk.
"""

import os
from pathlib import Path


def _find_repo_root(start: Path) -> Path:
    for parent in [start, *start.parents]:
        if (parent / "pyproject.toml").exists():
            return parent
    return Path.cwd()


REPO_ROOT = _find_repo_root(Path(__file__).resolve())
DATA_DIR = Path(os.environ.get("CLOCKS_DATA_DIR", REPO_ROOT / "data"))
