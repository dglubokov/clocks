# Aging Clocks

**A Comprehensive Collection of Aging Clocks: Historical Context, Implementation Details, and Critical Insights**

This repository provides a curated set of aging clock implementations, along with background information, theoretical underpinnings, and critical analyses. Aging clocks are powerful tools to estimate biological age from various biological data, and this collection aims to facilitate learning, research, and reproducibility by providing well-documented examples of popular models.

## Overview

- **What are aging clocks?**  
    Aging clocks are computational models that predict biological age based on molecular data, such as DNA methylation, gene expression, or other biomarkers. These models are trained on datasets with known chronological age labels to learn the relationship between molecular patterns and aging.

- **Why this repository?**  
  This repository compiles code implementations of well-known aging clocks, enabling researchers and practitioners to:
  - Understand the mathematical and biological foundations of each model.
  - Reproduce reported results and adapt the methods to new datasets.
  - Compare performance across different aging clock models.
  - Explore the historical development and critical commentary on their applications and limitations.

## Getting Started

### Prerequisites

- **Python**: Ensure you have Python 3.7+ installed.
- **Package Requirements**: Review the `requirements.txt` file and install the necessary packages `pip install -r requirements.txt`.
- **Jupyter**: For interactive exploration, install Jupyter Notebook or JupyterLab (link to [installation guide](https://jupyter.org/install)).
- **R**: Some notebooks may require R for specific analyses. Install R from the [official website](https://www.r-project.org/) and use the `IRkernel` package for Jupyter integration.
- **R Packages**: If R is required, install the necessary packages using `install.packages("package_name")` within an R environment.

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/dglubokov/clocks
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Navigate to a specific clock’s directory:**
   ```bash
   cd clocks/2013_Horvath
   ```


### Running the Notebook

1. Open the chosen clock’s Jupyter notebook (`.ipynb` file).
2. Run all cells in sequence to:
   - Load example datasets (if provided).
   - Train or apply the clock model.
   - Visualize results and metrics.

Some directories may contain additional scripts or more jupyter notebooks.

## Clocks Implemented

1. **[2011 Bocklandt Clock](/2011_Bocklandt/)**  
   Early epigenetic clock focused on DNA methylation changes associated with aging in human saliva samples.
   
2. **[2013 Horvath Clock](/2013_Horvath/)**  
   A pioneering pan-tissue epigenetic clock by Steve Horvath, widely cited and used for human aging studies.

## Contributing

Contributions are welcome! If you have a new aging clock implementation, improvements to existing code, or ideas for additional analyses, feel free to open a pull request or submit an issue.

## License

This repository is provided under the [MIT License](LICENSE). Please review the license file for more details.

## Acknowledgments

We gratefully acknowledge the authors of the original aging clocks, the research community for continuous development, and data contributors for making their datasets available for public research.
