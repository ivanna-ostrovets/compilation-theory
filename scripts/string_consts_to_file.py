import os
from re import sub, findall

from sys import argv


def convert_ascii(match):
    return chr(int(match.group(1)))


def string_consts_to_file(text):
    output = sub(r'(?<!\'{1})\'\s*\+\s*\'', '', text)
    output = sub(r'\'\s*#(\d+)\s*\'', convert_ascii, output)
    output = findall('(?<=\').*(?=\')', output)

    return '\n'.join(output)


if __name__ == '__main__':
    from file_operations import create_output_folder, read_file, write_to_file

    file_path = argv[1]
    file_name = os.path.basename(file_path)

    output_folder_path = '{}/output'.format(os.path.dirname(os.path.realpath(__file__)))
    create_output_folder(output_folder_path)

    text = string_consts_to_file(read_file(file_path))
    write_to_file(output_folder_path, file_name, text)
