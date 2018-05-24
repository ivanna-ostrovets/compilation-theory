from re import sub
from sys import argv

from scripts.expressions import enter_variables, infix_to_postfix
from scripts.file_operations import read_file_lines
from scripts.tree import Tree


def lab_6_7(expressions):
    print('*' * 50)

    for expression in expressions:
        print('Expression:', expression)

        expression = sub(r'\n', '', expression)
        expression = expression.split()
        expression = enter_variables(expression)
        expression = infix_to_postfix(expression)

        print('Expression in postfix (reverse Polish) notation:', ' '.join(expression))

        tree = Tree()
        tree.from_postfix(expression)
        tree.print()

        print('Calculated result:', tree.calculate(), '\n')
        print('*' * 50)


if __name__ == '__main__':
    if len(argv) > 1:
        file_path = argv[1]
        expressions = read_file_lines(file_path)
    else:
        expressions = ['( 2 + 3 ) * 4 - ( 5 - 6 ) * ( 7 + 8 )']

    lab_6_7(expressions)
