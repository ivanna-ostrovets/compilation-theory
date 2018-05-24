def print_tree(node):
    width, height, pos_root, block = pretty_tree(node)

    for value in block:
        print(value)


def pretty_tree(node):
    value = str(node.value)
    length = len(value)

    if node.left is None and node.right is None:
        return length, 1, length / 2, [value]

    bottom_left_block = []
    bottom_right_block = []

    left_width, right_width, left_height, right_height, left_depth, right_depth = 0, 0, 0, 0, 0, 0

    if node.left is not None:
        left_width, left_height, pos_root_left, block = pretty_tree(node.left)
        left_depth = left_width - pos_root_left
        slash = draw_left_slash(left_width, pos_root_left)
        bottom_left_block = slash + block

    if node.right is not None:
        right_width, right_height, pos_root_right, block = pretty_tree(node.right)
        right_depth = pos_root_right + 1
        slash = draw_right_slash(right_width, pos_root_right)
        bottom_right_block = slash + block

    total_left_height = left_height + left_depth
    total_right_height = right_height + right_depth

    max_height = max(total_left_height, total_right_height)

    if len(bottom_left_block) == 0:
        bottom_left_block = vertical_blank(max_height)
        left_width = 1

    if len(bottom_right_block) == 0:
        bottom_right_block = vertical_blank(max_height)
        right_width = 1

    new_left_height = len(bottom_left_block)
    new_right_height = len(bottom_right_block)
    bottom_left_block += blank(left_width, max(0, max_height - new_left_height))
    bottom_right_block += blank(right_width, max(0, max_height - new_right_height))

    top_line = horizontal_blank(left_width) + value + horizontal_blank(right_width)
    bottom_block = horizontal_concat(
        bottom_left_block,
        horizontal_concat(blank(length, max_height), bottom_right_block)
    )
    final_block = [top_line] + bottom_block

    return (
        left_width + length + right_width,
        max_height + 1,
        left_width + length / 2,
        final_block,
    )


def horizontal_blank(w):
    return " " * w


def vertical_blank(h):
    return [" "] * int(h)


def blank(width, heigth):
    return [horizontal_blank(width)] * int(heigth)


def horizontal_concat(str_list1, str_list2):
    return [s1 + s2 for s1, s2 in zip(str_list1, str_list2)]


def draw_left_slash(width, pos):
    if width == 1:
        return ["/"]

    d = int(width - pos)

    return [horizontal_blank(width - i - 1) + "/" + horizontal_blank(i) for i in range(d)]


def draw_right_slash(width, pos):
    if width == 1:
        return ["\\"]

    d = int(pos + 1)

    return [horizontal_blank(i) + "\\" + horizontal_blank(width - i - 1) for i in range(d)]
