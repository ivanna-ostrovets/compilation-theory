import os


def create_output_folder(output_folder_path):
    os.makedirs(output_folder_path, exist_ok=True)


def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()


def read_file_lines(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()


def write_to_file(output_folder_path, file_name, text):
    with open('{}/new_{}'.format(output_folder_path, file_name), 'w+') as new:
        new.write(text)
