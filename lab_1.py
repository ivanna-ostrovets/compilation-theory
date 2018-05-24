import os

from scripts.delete_comments import delete_comments
from scripts.single_operator_in_line import single_operator_in_line
from scripts.string_consts_to_file import string_consts_to_file
from scripts.file_operations import create_output_folder, read_file, write_to_file


if __name__ == '__main__':
    output_folder_path = '{}/output'.format(os.path.dirname(os.path.realpath(__file__)))
    create_output_folder(output_folder_path)

    file_1_path = './test_data/delete_comments_test.cpp'
    file_1_name = os.path.basename(file_1_path)
    result_1 = delete_comments(read_file(file_1_path))
    write_to_file(output_folder_path, file_1_name, result_1)

    file_2_path = './test_data/single_operator_in_line_test.pas'
    file_2_name = os.path.basename(file_2_path)
    result_2 = single_operator_in_line(read_file(file_2_path))
    write_to_file(output_folder_path, file_2_name, result_2)

    file_3_path = './test_data/string_consts_to_file_test.pas'
    file_3_name = os.path.basename(file_3_path)
    result_3 = string_consts_to_file(read_file(file_3_path))
    write_to_file(output_folder_path, file_3_name, result_3)
