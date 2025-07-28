# 3.1.

from glob import glob
import os
from PIL import Image


def image_converter(ext1, ext2):
    root_dir = os.path.join(os.getcwd(), "working_with_images")
    founded_files = glob(os.path.join(root_dir, f"*{ext1}"))
    for file in founded_files:
        im = Image.open(file)
        if im.mode == "RGBA":
            im = im.convert("RGB")
        im.save(f"{file.split('.')[0]}{ext2}")
