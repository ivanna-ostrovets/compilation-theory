from statistics import mean
from sys import argv
from time import time

from scripts.array import search, sort, binary_search, insert_in_sorted_array, full_array, random_array
from scripts.file_operations import read_file

ARRAY_SIZE = 1000
ARRAY_FULLNESS = ARRAY_SIZE * 0.9


def task_1(array, words_for_search):
    # Looks for 20 words in a not sorted array
    # Evaluates the time of the search and number of comparisons

    search_times = []
    search_comparisons = []

    print('_' * 50)
    print('\nSEARCH\n')

    for index, word in enumerate(words_for_search):
        start_time = time()
        searched_index, comparisons = search(array, word)
        elapsed_time = time() - start_time

        search_times.append(elapsed_time)
        search_comparisons.append(comparisons)

        print('Round #', index + 1)
        print('Index of a searched word:', searched_index)
        print('Comparisons:', comparisons)
        print('Time:', '{:.10f}'.format(elapsed_time), 's')
        print('*' * 20)

    print('\nAverage time:', '{:.10f}'.format(mean(search_times)), 's')
    print('Average comparisons:', mean(search_comparisons))
    print('_' * 50)


def task_2(old_array):
    # Sorts the array
    # Evaluates sorting time and number of comparisons and permutations

    array = list(old_array)

    print('\nSORT\n')

    start_time = time()
    array, comparisons, permutations = sort(array)
    elapsed_time = time() - start_time

    print('Comparisons:', comparisons)
    print('Permutations:', permutations)
    print('Time:', '{:.10f}'.format(elapsed_time), 's')
    print('_' * 50)

    return array


def task_3(array, words_for_search):
    # Looks for 20 words in a sorted array using binary search
    # Evaluates the time of the search and number of comparisons

    print('\nBINARY SEARCH\n')

    search_times = []
    search_comparisons = []

    for index, word in enumerate(words_for_search):
        start_time = time()
        searched_index, comparisons = binary_search(array, word)
        elapsed_time = time() - start_time

        search_times.append(elapsed_time)
        search_comparisons.append(comparisons)

        print('Round #', index + 1)
        print('Index of a searched word:', searched_index)
        print('Comparisons:', comparisons)
        print('Time:', '{:.10f}'.format(elapsed_time), 's')
        print('*' * 20)

    print('\nAverage time:', '{:.10f}'.format(mean(search_times)), 's')
    print('Average comparisons:', mean(search_comparisons))
    print('_' * 50)


def task_4(old_array, words_for_insert):
    # Adds new 10 words to the sorted array without breaking orderliness
    # Evaluates insertion time and number of comparisons and permutations

    array = list(old_array)
    search_times = []
    insert_comparisons = []
    insert_permutations = []

    print('\nINSERT IN A SORTED ARRAY\n')

    for index, word in enumerate(words_for_insert):
        start_time = time()
        array, comparisons, permutations = insert_in_sorted_array(array, word)
        elapsed_time = time() - start_time

        search_times.append(elapsed_time)
        insert_comparisons.append(elapsed_time)
        insert_permutations.append(comparisons)

        print('Round #', index + 1)
        print('Comparisons:', comparisons)
        print('Permutations:', permutations)
        print('Time:', '{:.10f}'.format(elapsed_time), 's')
        print('*' * 20)

    print('\nAverage time:', '{:.10f}'.format(mean(search_times)), 's')
    print('Average comparisons:', mean(insert_comparisons))
    print('Average permutations:', mean(insert_permutations))
    print('_' * 50)

    return array


if __name__ == '__main__':
    if len(argv) > 1:
        file_path = argv[1]
    else:
        file_path = './test_data/lab_2_test.txt'

    text = read_file(file_path)
    words = text.split()
    array = full_array(words, ARRAY_SIZE, ARRAY_FULLNESS)

    words_for_search = random_array(array, 20)
    words_for_insert = random_array(array, 10)

    task_1(array, words_for_search)
    array = task_2(array)
    task_3(array, words_for_search)
    array = task_4(array, words_for_insert)
