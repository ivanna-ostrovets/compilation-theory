from scripts.expressions import OPERATORS
from scripts.tree import Tree

# tree_nodes = {
#     'data': '+',
#     'left': {
#         'data': '-',
#         'left': {
#             'data': '*',
#             'left': {'data': 2},
#             'right': {'data': 3},
#         },
#         'right': {'data': '5'},
#     },
#     'right': {
#         'data': '/',
#         'left': {
#             'data': '^',
#             'left': {'data': 2},
#             'right': {'data': 3},
#         },
#         'right': {'data': 4},
#     },
# }
#
# tree = Tree()
# tree.from_object(tree_nodes)
# tree.print()
#
# print('\nCalculated result:', tree.calculate())

expression = []

node = input('Enter root element ({}): '.format(', '.join(OPERATORS)))
expression.append(node)

print('Enter tree nodes (all left firstly). Enter q for exit.')

while True:
    node = input('Enter node ({} or numbers, q to quit): '.format(', '.join(OPERATORS)))

    if node is 'q':
        break

    expression.append(node)

tree = Tree()
tree.from_prefix(expression)
tree.print()

print('\nCalculated result:', tree.calculate())
