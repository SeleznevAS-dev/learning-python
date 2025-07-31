"Solution of task 'working with image' topic."

# 3.1.

from glob import glob
import os
from PIL import Image, ImageDraw


def image_converter(ext1, ext2):
    "Function for converting from ext1 to ext2."
    root_dir = os.path.join(os.getcwd(), "working_with_images")
    founded_files = glob(os.path.join(root_dir, f"*{ext1}"))
    for file in founded_files:
        im = Image.open(file)
        if im.mode == "RGBA":
            im = im.convert("RGB")
        im.save(f"{file.split('.')[0]}{ext2}")


# 3.2.
def image_converter_modified(ext1, ext2):
    "Modified function for converting files"
    root_dir = os.path.join(os.getcwd(), "working_with_images")
    founded_files = glob(os.path.join(root_dir, f"*{ext1}"))
    for file in founded_files:
        im = Image.open(file)
        if im.mode == "RGBA":
            im = im.convert("RGB")
        sz = im.size
        draw = ImageDraw.Draw(im)

        draw.rectangle(
            [
                sz[0] // 2 - sz[1] // 8,
                sz[1] // 2 - sz[1] // 8,
                sz[0] // 2 + sz[1] // 8,
                sz[1] // 2 + sz[1] // 8,
            ],
            outline=(0, 0, 0),
            width=10,
        )
        draw.multiline_text(
            (sz[0] // 2 - sz[1] // 16, sz[1] // 2 - sz[1] // 16),
            "Hello,\nWorld!",
            fill=(0, 0, 0),
            font_size=50,
        )
        im.save(f"{file.split('.')[0]}{ext2}")
        del draw
