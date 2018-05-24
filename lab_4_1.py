from re import sub
from sys import argv

from scripts.expressions import enter_variables, calculate_prefix
from scripts.file_operations import read_file_lines


def lab_4_1(expressions):
    print('*' * 50)

    for expression in expressions:
        expression = sub(r'\n', '', expression)
        expression = expression.split()

        print('Expression:', expression)
        expression = enter_variables(expression)
        print('Calculated result:', calculate_prefix(expression), '\n')
        print('*' * 50)


if __name__ == '__main__':
    if len(argv) > 1:
        file_path = argv[1]
    else:
        file_path = './test_data/lab_4_1_test.txt'

    expressions = read_file_lines(file_path)
    lab_4_1(expressions)
