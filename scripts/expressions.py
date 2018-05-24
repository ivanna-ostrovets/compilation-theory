import operator

from math import sqrt
from pythonds import Stack

OPERATORS = {
    '+':  operator.add,
    '-':  operator.sub,
    '*': operator.mul,
    '/':  operator.truediv,
    '%':  operator.mod,
    '^': operator.pow,
    '||': operator.abs,
    'sqrt': sqrt,
}
OPERATORS_KEYS = OPERATORS.keys()
OPERATORS_PRECEDENCE = {'^': 4, '*': 3, '/': 3, '+': 2, '-': 2, '(': 1}


def calculate_prefix(expression):
    expression = list(reversed(expression))

    while len(expression) > 1:
        for index, value in enumerate(expression):
            length = len(expression)

            if (length == 3
                    and index + 1 < length
                    and index + 2 < length
                    and expression[index + 1] == '='):
                return equality_string(index, value, expression)

            if (is_number(value)
                    and index + 1 < length
                    and index + 2 < length
                    and is_number(expression[index + 1])
                    and expression[index + 2] in OPERATORS_KEYS):
                expression[index] = OPERATORS[expression[index + 2]](
                    float(expression[index + 1]),
                    float(value),
                )

                del expression[index + 1]
                del expression[index + 1]

                continue

    return expression[0]


def calculate_posfix(expression):
    while len(expression) > 1:
        for index, value in enumerate(expression):
            length = len(expression)

            if (length == 3
                    and index + 1 < length
                    and index + 2 < length
                    and expression[index + 1] == '='):
                return equality_string(index, value, expression)

            if (is_number(value)
                    and index + 1 < length
                    and index + 2 < length
                    and is_number(expression[index + 1])
                    and expression[index + 2] in OPERATORS_KEYS):
                expression[index] = OPERATORS[expression[index + 2]](
                    float(value),
                    float(expression[index + 1]),
                )

                del expression[index + 1]
                del expression[index + 1]

                continue

    return expression[0]


def equality_string(index, value, expression):
    return '{} ({})'.format(
        ' '.join(str(value) for value in expression),
        float(value) == float(expression[index + 2]),
    )


def enter_variables(expression):
    operators = ['=', '(', ')']
    operators.extend(OPERATORS_KEYS)

    for index, value in enumerate(expression):
        if not is_number(value) and value not in operators:
            expression[index] = input('Please enter variable {}: '.format(value))

    return expression


def infix_to_postfix(token_list):
    stack = Stack()
    postfix_list = []

    for token in token_list:
        if token.isalpha() or token.isdecimal():
            postfix_list.append(token)

        elif token == '(':
            stack.push(token)

        elif token == ')':
            top_token = stack.pop()

            while top_token != '(':
                postfix_list.append(top_token)
                top_token = stack.pop()

        else:
            while not stack.isEmpty() and OPERATORS_PRECEDENCE[stack.peek()] >= OPERATORS_PRECEDENCE[token]:
                postfix_list.append(stack.pop())

            stack.push(token)

    while not stack.isEmpty():
        postfix_list.append(stack.pop())

    return postfix_list


def is_number(number):
    try:
        float(number)
        return True
    except ValueError:
        return False
