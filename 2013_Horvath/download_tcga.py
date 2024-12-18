import json
from pathlib import Path

import requests
import pandas as pd
from tqdm import tqdm

BASE_URL = "https://api.gdc.cancer.gov"
BASE_DATA_DIR = Path("data/TCGA")

BASE_DATA_DIR.mkdir(parents=True, exist_ok=True)


def main():
    url = "https://static-content.springer.com/esm/art%3A10.1186%2Fgb-2013-14-10-r115/MediaObjects/13059_2013_3156_MOESM1_ESM.csv"
    dataset_meta = pd.read_csv(url, encoding="latin1")

    tcga_set = dataset_meta.loc[dataset_meta["Availability"] == "TCGA", "Citation"].str.replace(", ", "-").unique()
    for tcga_id in tqdm(tcga_set):
        fetch_tcga_data(tcga_id)


def fetch_tcga_data(tcga_id):
    filters = {
        "op": "and",
        "content": [
            {"op": "in", "content": {"field": "cases.project.project_id", "value": [tcga_id]}},
            {"op": "in", "content": {"field": "data_category", "value": ["DNA Methylation"]}},
        ],
    }

    # Construct the parameters for the GDC API request
    params = {
        "filters": json.dumps(filters),
        "fields": "file_id,file_name",
        "format": "JSON",
        "size": 10000,  # Set to a large number to ensure all files are returned
    }

    # Query the GDC API for file metadata
    response = requests.get(f"{BASE_URL}/files", params=params)
    if response.status_code != 200:
        print("Error querying the GDC API. Status code:", response.status_code)
        return
    else:
        print("Query successful.")

    # Parse the JSON response which contains metadata of the matched files
    data = response.json()
    hits = data.get("data", {}).get("hits", [])
    if not hits:
        print("No files found for the given criteria. Consider adjusting the filters.")
        return
    else:
        print(f"Found {len(hits)} files matching the criteria.")

    # Download each file returned by the query
    file_dir = BASE_DATA_DIR / tcga_id
    if file_dir.exists():
        # Force remove the directory and its contents
        for file in file_dir.iterdir():
            file.unlink()
    file_dir.mkdir(parents=True, exist_ok=True)
    for file_info in hits:
        file_id = file_info["file_id"]
        file_name = file_info["file_name"]
        download_url = f"{BASE_URL}/data/{file_id}"

        # Perform the actual file download
        dl_response = requests.get(download_url, stream=True)
        if dl_response.status_code == 200:
            file_path = file_dir / file_name
            with open(file_path, "wb") as f:
                for chunk in dl_response.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
            print(f"Downloaded file: {file_path}")
        else:
            print(f"Failed to download file {file_id}. Status code: {dl_response.status_code}")

    print(f"Downloaded all files for TCGA project: {tcga_id}")
    return


if __name__ == "__main__":
    main()
