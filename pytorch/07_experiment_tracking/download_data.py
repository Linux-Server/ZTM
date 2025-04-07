import os
import zipfile
import requests
from pathlib import Path

def download_data(source:str,
                  destination : str,
                  remove_source: bool = True
                  ) -> Path : 
    """Download a zip dataset from source and upzip and keep it in destination"""
    data_path = Path("data")
    image_path =  data_path/destination

    # if image path doesnt exist creeat one

    if image_path.is_dir():
        print(f"[INFO] Directory exist skip download")
    else:
        image_path.mkdir(parents=True, exist_ok=True)

        target_file = Path(source).name

        # download the zip file
        with open(data_path/target_file, "wb") as f:
            res = requests.get(source)
            f.write(res.content)



    # Now unzip the file
    with zipfile.ZipFile(data_path/target_file, "r") as zp:
        print("Unzipping file..")
        zp.extractall(image_path)


    return image_path

