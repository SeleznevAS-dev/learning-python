import unittest
import os
from working_with_images.working_with_images import image_converter
from PIL import Image


class WorkingWithFilesTests(unittest.TestCase):
    # 3.1.
    def test_regression_convert_image(self):
        test_dir = os.path.join(os.getcwd(), "working_with_images")

        test_png_path = os.path.join(test_dir, "test_image.png")
        test_jpg_path = os.path.join(test_dir, "test_image.jpg")

        try:
            img = Image.new("RGB", (100, 100), color=(100, 100, 100))
            img.save(test_png_path)

            image_converter(".png", ".jpg")

            self.assertTrue(os.path.exists(test_jpg_path))

        finally:
            if os.path.exists(test_png_path):
                os.remove(test_png_path)
            if os.path.exists(test_jpg_path):
                os.remove(test_jpg_path)


if __name__ == "__main__":
    unittest.main()
