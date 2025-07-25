from zipfile import ZipFile
import os
from glob import glob


def write_zip(filename, ext):
    root_dir = os.path.join(os.getcwd(), "working_with_zips")
    with ZipFile(f"{root_dir}/{filename}.zip", "w") as zipfile:
        founded_files = glob(os.path.join(root_dir, f"*{ext}"))
        for file in founded_files:
            zipfile.write(file, os.path.basename(file))
