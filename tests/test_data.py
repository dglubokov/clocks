import gzip

from clocks.data import geo_url, read_geo_series_matrix

MATRIX = """\
!Series_title\t"Toy"
!Sample_title\t"111"\t"112"
!Sample_geo_accession\t"GSM1"\t"GSM2"
!Sample_characteristics_ch1\t"pair id number: 1"\t"pair id number: 1"
!Sample_characteristics_ch1\t"age: 40"\t"age: 41"
!Sample_characteristics_ch1\t"tissue: blood"\t"sex: F"
!series_matrix_table_begin
"ID_REF"\t"GSM1"\t"GSM2"
"cg01"\t0.1\t0.2
"cg02"\t0.9\t
!series_matrix_table_end
"""


def test_read_geo_series_matrix(tmp_path):
    path = tmp_path / "toy_series_matrix.txt.gz"
    with gzip.open(path, "wt") as f:
        f.write(MATRIX)

    samples, values = read_geo_series_matrix(path)

    assert list(samples.index) == ["GSM1", "GSM2"]
    assert list(samples["age"]) == ["40", "41"]
    assert list(samples["pair id number"]) == ["1", "1"]
    # Mixed keys on one line are kept raw instead of being mislabelled.
    assert list(samples["characteristics_ch1"]) == ["tissue: blood", "sex: F"]

    assert values.shape == (2, 2)
    assert values.loc["cg01", "GSM2"] == 0.2
    assert values["GSM2"].isna().sum() == 1


def test_geo_url():
    assert geo_url("GSE28746", "x.txt.gz") == (
        "https://ftp.ncbi.nlm.nih.gov/geo/series/GSE28nnn/GSE28746/matrix/x.txt.gz"
    )
    assert "/GSE1nnn/GSE1234/suppl/" in geo_url("GSE1234", "f", kind="suppl")
