# Aging Clocks — a course on real data

This repository is being rebuilt from scratch as a teaching course on aging clocks. We reproduce the original papers on public data and critique them. The pre-rebuild code (2011_Bocklandt/, 2013_Horvath/) is legacy: use it for reference only.

## Conventions
- **Language:** all course material (notebooks, README, comments) is in English. Discussion with the user happens in Russian.
- **Audience is mixed** (biologists and ML people): explain both the biology and the statistics, and don't assume either background.
- **Python or R,** whichever is the natural tool for the step (e.g. WGCNA, minfi or sesame in R; sklearn in Python).
- **Order is chronological,** by publication date. One paper at a time, iteratively.
- Notebook template: question → what the authors did → data → method → reproduce key figure/table → compare with the original → where it breaks → exercises → references.
- References are cited by DOI; a shared `references.bib` is planned.
- No website yet (Jupyter Book or Quarto later, maybe).

## Git
- **Never commit or push. Never create tags.** The user does all of that. Prepare changes step by step in the working tree, then give a short summary and a suggested commit message.

## Layout
- `notebooks/<YEAR>_<Author>/`: chapters. Keep outputs in committed notebooks so they read well on GitHub.
- `src/clocks/`: shared plumbing (`data.py`: download/cache, GEO series matrix parser). Put logic here only when a second chapter needs it; the science stays in notebooks.
- `data/`: cache (gitignored; override with `CLOCKS_DATA_DIR`).
- Python: `uv sync`, `uv run pytest`, `uv run ruff check`. R: `uv run Rscript R/install.R` (Bioconductor 3.22, IR kernel).
- `references.bib`: check every DOI against Crossref (`https://api.crossref.org/works/<doi>`) before adding it.

## Literature workflow (`papers/`, gitignored — never commit)
For each paper, `papers/<YEAR>_<FirstAuthor>/` contains:
- `paper.pdf`: the original, which the user adds or Claude downloads when open access;
- `paper.txt`: raw text extraction (`uv run --no-project --with pymupdf ...`);
- `supplement/`: supplementary tables and methods;
- `notes.md`: Claude's notes, meaning key claims with numbers and page references, discrepancies with public data, reproducibility targets, pitfalls, and ideas for the notebook.

Before writing a course notebook, read the paper's `notes.md`. Check claims against `paper.txt` rather than memory.
