import unittest
import os
from zipfile import ZipFile
from working_with_zips.working_with_zips import write_zip


class WorkingWithZipsTests(unittest.TestCase):
    def test_write_zip(self):
        test_dir = os.path.join(os.getcwd(), "working_with_zips")

        try:
            with open(os.path.join(test_dir, "1.txt"), "wt") as f:
                f.write("")

            write_zip("test", ".txt")

            zip_path = os.path.join(test_dir, "test.zip")
            self.assertTrue(os.path.exists(zip_path))

            with ZipFile(zip_path, "r") as zf:
                files = zf.namelist()
                self.assertEqual(len(files), 1)
                self.assertIn("1.txt", files)

        finally:
            if os.path.exists(os.path.join(test_dir, "1.txt")):
                os.remove(os.path.join(test_dir, "1.txt"))
            if os.path.exists(zip_path):
                os.remove(zip_path)


if __name__ == "__main__":
    unittest.main()
