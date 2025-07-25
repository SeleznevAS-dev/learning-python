import unittest
import os
import shutil
from working_with_files_2.working_with_files_2 import dirs_and_files, delete_dir


class WorkingWithFiles2Tests(unittest.TestCase):
    # 4.1
    def test_regression_get_dirs_and_files(self):
        test_dir = "test_temp_dir"
        try:
            os.makedirs(os.path.join(test_dir, "dir1"))
            os.makedirs(os.path.join(test_dir, "dir2"))
            
            os.makedirs(os.path.join(test_dir, "dir1", "subdir1"))
            os.makedirs(os.path.join(test_dir, "dir2", "subdir2"))
            
            with open(os.path.join(test_dir, "1.txt"), "wt") as f:
                f.write("test")
            with open(os.path.join(test_dir, "1.py"), "wt") as f:
                f.write("test")
            with open(os.path.join(test_dir, "2.txt"), "wt") as f:
                f.write("test")

            with open(os.path.join(test_dir, "dir1", "4.txt"), "wt") as f:
                f.write("test")
            with open(os.path.join(test_dir, "dir2", "5.py"), "wt") as f:
                f.write("test")
            
            dirs1, files1 = dirs_and_files(test_dir, ".txt", True)
            dirs2, files2 = dirs_and_files(test_dir, ".py", False)

            self.assertEqual(dirs1, ["dir1", "dir2", "subdir1", "subdir2"])
            self.assertEqual(files1, ["1.txt", "2.txt", "4.txt"])
            self.assertEqual(dirs2, ["dir1", "dir2"])
            self.assertEqual(files2, ["1.py"])
        finally:
            if os.path.exists(test_dir):
                shutil.rmtree(test_dir)
    # 4.2    
    def test_regression_delete_dir_with_files(self):
        test_dir = "test_temp_dir2"
        try:
            test_subdir1 = os.path.join(test_dir, "with_files_only")
            os.makedirs(test_subdir1)
            
            with open(os.path.join(test_subdir1, "file1.txt"), "wt") as f:
                f.write("test")
            with open(os.path.join(test_subdir1, "file2.txt"), "wt") as f:
                f.write("test")
            
            result1 = delete_dir(test_subdir1)
            
            self.assertTrue(result1)
            self.assertFalse(os.path.exists(test_subdir1))
            
            test_subdir2 = os.path.join(test_dir, "with_subdirs")
            os.makedirs(test_subdir2)
            os.makedirs(os.path.join(test_subdir2, "subdir"))
            
            with open(os.path.join(test_subdir2, "file1.txt"), "wt") as f:
                f.write("test")
            
            result2 = delete_dir(test_subdir2)
            
            self.assertFalse(result2)
            self.assertTrue(os.path.exists(test_subdir2))
            
        finally:
            if os.path.exists(test_dir):
                shutil.rmtree(test_dir)


if __name__ == "__main__":
    unittest.main()
