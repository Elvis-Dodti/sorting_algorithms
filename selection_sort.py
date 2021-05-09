def selection_sort(unordered_list: list):
    """
    Sorts unordered lists.

    :param unordered_list: Unsorted list to sort.
    :return: Sorted list.
    """
    for index in range(len(unordered_list)):
        min_index = index
        for j in range(index + 1, len(unordered_list)):
            if unordered_list[min_index] > unordered_list[j]:
                min_index = j
        # swap the minimum value with the compared value:
        unordered_list[index], unordered_list[min_index] = unordered_list[min_index], unordered_list[index]


demo = [23, 45, 12, 31, 58, 34, 98, 65, 78]
selection_sort(demo)
print(demo)
