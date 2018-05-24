from scripts.draw_tree import print_tree
from scripts.expressions import calculate_prefix, OPERATORS_PRECEDENCE


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Tree(object):
    def __init__(self, ):
        self.nodes_array = []
        self.root = None

    def from_postfix(self, expression):
        stack = []

        for value in expression:
            if value not in OPERATORS_PRECEDENCE:
                node = Node(value)
                stack.append(node)
            else:
                node = Node(value)
                node.right = stack.pop()
                node.left = stack.pop()
                stack.append(node)

        self.root = stack.pop()

    def from_prefix(self, expression):
        if len(expression) > 0:
            self.root = Node(expression[0])

        if len(expression) > 1:
            self._from_prefix(self.root, expression[1:])

    def _from_prefix(self, node, expression):
        if node.left is None:
            node.left = Node(expression.pop(0))
            if len(expression) > 1:
                self._from_prefix(node.left if node.left.value in OPERATORS_PRECEDENCE else node, expression)

        if node.right is None:
            node.right = Node(expression.pop(0))
            if len(expression) > 1:
                self._from_prefix(node.right if node.right.value in OPERATORS_PRECEDENCE else node, expression)

    def from_object(self, obj):
        self.root = Node(obj['data'])
        self._from_object(self.root, obj)

    def _from_object(self, node, obj):
        if 'left' in obj:
            node.left = Node(obj['left']['data'])
            self._from_object(node.left, obj['left'])

        if 'right' in obj:
            node.right = Node(obj['right']['data'])
            self._from_object(node.right, obj['right'])

    def preorder(self, node):
        if node is None:
            return

        self.nodes_array.append(node.value)

        self.preorder(node.left)
        self.preorder(node.right)

    def postorder(self, node):
        if node is None:
            return

        self.postorder(node.left)
        self.postorder(node.right)

        self.nodes_array.append(node.value)

    def inorder(self, node):
        if node is None:
            return

        self.inorder(node.left)

        self.nodes_array.append(node.value)

        self.inorder(node.right)

    def calculate(self):
        self.preorder(self.root)

        return calculate_prefix(self.nodes_array)

    def print(self):
        print_tree(self.root)