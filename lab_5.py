import re
from statistics import mean
from sys import argv

from scripts.file_operations import read_file_lines
from scripts.hash import hash_1, hash_2, hash_3, hash_4, rehesh


def set_array_value(array, array_length, value, hash_value, collisions):
    if array[hash_value] is None:
        array[hash_value] = value

        return collisions
    else:
        collisions += 1
        hash_value = rehesh(hash_value, array_length)

        return set_array_value(array, array_length, value, hash_value, collisions)


def full_array(old_array, array_length, hash, values):
    array = list(old_array)
    collisions = 0
    comparisons = []

    for value in values:
        hash_value = hash(value, array_length)
        result_collisions = set_array_value(array, array_length, value, hash_value, 0)
        collisions += result_collisions
        comparisons.append(result_collisions)

    return array, collisions, comparisons


def lab_5(hash, file_path_1, file_path_2):
    array_length = 128
    array = [None] * array_length

    values = read_file_lines(file_path_1)

    for index, value in enumerate(values):
        values[index] = re.sub(r'\n', '', value)

    array, collisions, comparisons = full_array(array, array_length, hash, values)

    values = read_file_lines(file_path_2)

    for index, value in enumerate(values):
        values[index] = re.sub(r'\n', '', value)

    array, collisions, comparisons = full_array(array, array_length, hash, values)

    print('{}, collisions: {}, average comparisons: {}'.format(hash.__name__, collisions, mean(comparisons)))


if __name__ == '__main__':
    if len(argv) > 2:
        file_path_1 = argv[1]
        file_path_2 = argv[2]
    else:
        file_path_1 = './test_data/lab_5_1_test.txt'
        file_path_2 = './test_data/lab_5_2_test.txt'

    lab_5(hash_1, file_path_1, file_path_2)
    lab_5(hash_2, file_path_1, file_path_2)
    lab_5(hash_3, file_path_1, file_path_2)
    lab_5(hash_4, file_path_1, file_path_2)
