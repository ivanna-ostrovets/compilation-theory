import os

from re import sub
from sys import argv


def delete_comments(text):
    output = sub(r'\s+//.*\s', '\n', text)
    output = sub(r'\s*/\*\s*.*\s*\*/', '', output)
    output = sub(r'\n{3,}', '\n\n', output)

    return output


if __name__ == '__main__':
    from file_operations import create_output_folder, read_file, write_to_file

    file_path = argv[1]
    file_name = os.path.basename(file_path)

    output_folder_path = '{}/output'.format(os.path.dirname(os.path.realpath(__file__)))
    create_output_folder(output_folder_path)

    text = delete_comments(read_file(file_path))
    write_to_file(output_folder_path, file_name, text)
