import os

from re import sub, escape
from sys import argv


PASCAL_OPERATORS = [
    '+', '-', '*', '/', '%',                   # Arithmetic Operators
    '=', '<>', '>', '<', '>=', '<=', '><',     # Relational Operators
    '&', '|', '!', '~', '<<', '>>',            # Bit Operators
    ':=', ';',
    'and', 'and then', 'or', 'or else', 'not'  # Boolean Operators
]


def single_operator_in_line(text, operators=PASCAL_OPERATORS):
    output = text

    for operator in operators:
        if operator in text:
            output = sub(r'{}'.format(escape(operator)), '\g<0>\n', output)

    return output


if __name__ == '__main__':
    from file_operations import create_output_folder, read_file, write_to_file

    file_path = argv[1]
    file_name = os.path.basename(file_path)

    output_folder_path = '{}/output'.format(os.path.dirname(os.path.realpath(__file__)))
    create_output_folder(output_folder_path)

    text = single_operator_in_line(read_file(file_path))
    write_to_file(output_folder_path, file_name, text)
