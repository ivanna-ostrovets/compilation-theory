from re import sub
from sys import argv

from scripts.expressions import enter_variables, infix_to_postfix, calculate_posfix
from scripts.file_operations import read_file_lines


def lab_4_2(expressions):
    print('*' * 50)

    for expression in expressions:
        print('Expression:', expression)
        expression = sub(r'\n', '', expression)
        expression = expression.split()
        expression = enter_variables(expression)
        expression = infix_to_postfix(expression)
        print('Expression in postfix (reverse Polish) notation:', ' '.join(expression))
        print('Calculated result:', calculate_posfix(expression), '\n')
        print('*' * 50)


if __name__ == '__main__':
    if len(argv) > 1:
        file_path = argv[1]
    else:
        file_path = './test_data/lab_4_2_test.txt'

    expressions = read_file_lines(file_path)
    lab_4_2(expressions)
