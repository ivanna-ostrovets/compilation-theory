from random import sample


def full_array(words, array_size, array_fullness):
    array = [''] * array_size

    for index, word in enumerate(words):
        if index > array_fullness:
            break

        array[index] = word

    return array


def search(array, word):
    comparisons = 0
    searched_index = None

    for index, item in enumerate(array):
        comparisons += 1

        if item == word:
            searched_index = index
            break

    return searched_index, comparisons


def sort(old_array):
    array = list(old_array)
    comparisons = 0
    permutations = 0

    for round in range(len(array) - 1, 0, -1):
        for i in range(round):
            comparisons += 1

            if array[i + 1] and array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                permutations += 1

    return array, comparisons, permutations


def binary_search(array, word):
    comparisons = 0
    searched_index = None
    lower_bound = 0
    upper_bound = len(array)

    while lower_bound != upper_bound:
        middle = (lower_bound + upper_bound) // 2

        if word == array[middle]:
            comparisons += 1
            searched_index = middle
            break
        elif array[middle] and word < array[middle]:
            comparisons += 1
            upper_bound = middle
        else:
            lower_bound = middle + 1

    return searched_index, comparisons


def insert_in_sorted_array(old_array, word):
    array = list(old_array)
    comparisons = 0
    permutations = 0
    i = len(array)
    array.append(word)

    while i > 0 and word < array[i - 1]:
        comparisons += 1
        permutations += 1
        array[i] = array[i - 1]
        i -= 1

    array[i] = word
    permutations += 1

    return array, comparisons, permutations


def random_array(array, number):
    return sample(list(filter(lambda a: a, array)), number)
