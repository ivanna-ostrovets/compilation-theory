import os
import shutil


def clean_output(path, dirs_to_remove):
    for root, dirs, files in os.walk(path):
        for dir in dirs:
            if dir in dirs_to_remove:
                shutil.rmtree(root + "/" + dir)


if __name__ == '__main__':
    path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    dirs_to_remove = ['output']

    clean_output(path, dirs_to_remove)
