# Install the R packages used in the course notebooks.
#
#   Rscript R/install.R
#
# Tested with R 4.5 / Bioconductor 3.22. Notebooks using R run on the IRkernel
# ("ir") Jupyter kernel; the script registers it if missing.

options(repos = c(CRAN = "https://cloud.r-project.org"))

if (!requireNamespace("BiocManager", quietly = TRUE)) install.packages("BiocManager")
BiocManager::install(version = "3.22", ask = FALSE, update = FALSE)

cran <- c(
  "IRkernel",
  "WGCNA",      # weighted correlation network analysis (Bocklandt 2011, Horvath 2013)
  "glmnet",     # elastic net as used by Horvath / Hannum
  "pheatmap",
  "data.table",
  "readxl"
)

bioc <- c(
  "limma",
  "sva",        # ComBat batch correction
  "qvalue",     # Storey q-values
  "GEOquery",
  "impute",     # WGCNA dependency
  "preprocessCore",
  "GO.db"
)

missing <- setdiff(c(cran, bioc), rownames(installed.packages()))
if (length(missing)) BiocManager::install(missing, ask = FALSE, update = FALSE)

# Register the R kernel for Jupyter. Run from the activated project env
# (`uv run Rscript R/install.R`) so that `jupyter` is on PATH.
tryCatch(
  IRkernel::installspec(name = "ir", displayname = "R"),
  error = function(e) message("Could not register the IR kernel: ", conditionMessage(e))
)

writeLines(capture.output(sessionInfo()), "R/sessionInfo.txt")
message("Done. Session info written to R/sessionInfo.txt")
