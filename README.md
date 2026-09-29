# Aging Clocks

**A hands-on course on biological aging clocks, reproduced on real public data.**

Aging clocks are statistical models that estimate age from molecular measurements, most famously DNA methylation. This course goes through the literature **in the order it was published**. For each landmark paper we:

1. explain the biological and statistical question it asked;
2. download the original public data;
3. reproduce the key tables and figures and **compare our numbers with the published ones**;
4. show where the method breaks: data leakage, batch effects, cell composition, overfitting;
5. end with exercises and references.

The course is written for a mixed audience. Biologists get the statistics and machine learning explained; ML practitioners get the biology explained. Each step uses whichever language is the natural tool for it: Python (pandas, scikit-learn) or R (WGCNA, limma, Bioconductor).

> **Status:** rebuilding from scratch. The previous version of this repository is available under the git tag `legacy`.

## Chapters

| # | Paper | Data | Topics | Status |
|---|---|---|---|---|
| 1 | Bocklandt et al. 2011, *Epigenetic predictor of age* ([doi](https://doi.org/10.1371/journal.pone.0014821)) | GSE28746, saliva, 27k | methylation arrays, beta values, twins and technical replicates, q-values, WGCNA, leave-one-out, **data leakage** | in progress |

More chapters will be added chronologically (Koch & Wagner 2011, Garagnani 2012, Hannum 2013, Horvath 2013, …).

## Repository layout

```
notebooks/<YEAR>_<Author>/   course chapters (Jupyter, Python or R kernel)
src/clocks/                  small shared package: downloading, caching, parsing
R/install.R                  R / Bioconductor dependencies
references.bib               bibliography for all chapters
tests/                       tests for the shared package
data/                        downloaded data cache (created on first run, not in git)
```

## Setup

**Python** uses [uv](https://docs.astral.sh/uv/). The lock file pins every version.

```bash
git clone https://github.com/dglubokov/clocks
cd clocks
uv sync                      # creates .venv with all dependencies
uv run jupyter lab
```

**R** is needed for some chapters. Install R ≥ 4.5 from [r-project.org](https://www.r-project.org/), then run:

```bash
uv run Rscript R/install.R   # Bioconductor packages + registers the "R" Jupyter kernel
```

Data is downloaded automatically on first use and cached in `data/`. Set `CLOCKS_DATA_DIR` to put the cache somewhere else.

## Contributing

Issues and pull requests are welcome, especially corrections to the science.

## License

Code and text: [MIT](LICENSE). The datasets and papers belong to their authors and are used under their original terms. Please cite the original papers.
