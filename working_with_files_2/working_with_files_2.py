# 4.1.
import os


def get_dirs_and_files(path, ext):
    dirs_list = []
    files_list = []
    dirs_and_files = os.listdir(path)
    for f in dirs_and_files:
        if os.path.isdir(os.path.join(path, f)):
            dirs_list.append(f)
        else:
            if f".{f.split('.')[-1]}" == ext:
                files_list.append(f)

    return dirs_list, files_list


def dirs_and_files(path, ext, flag):
    dirs = []
    files = []
    dirs_list, files_list = get_dirs_and_files(path, ext)
    dirs.extend(dirs_list)
    files.extend(files_list)
    if flag:
        for dir_name in dirs_list:
            new_dirs, new_files = get_dirs_and_files(os.path.join(path, dir_name), ext)
            dirs.extend(new_dirs)
            files.extend(new_files)

    return dirs, files
