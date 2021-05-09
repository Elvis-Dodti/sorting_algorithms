def insertion_sort(unordered_list: list) -> list:
    """
    Sorts the unordered list.

    :param unordered_list: Unsorted list to sort.
    :return: sorted list.
    """
    for i in range(1, len(unordered_list)):
        j = i - 1
        nxt_element = unordered_list[i]
        # compare the current element with the next one.
        while (unordered_list[j] > nxt_element) and (j >= 0):
            unordered_list[j + 1] = unordered_list[j]
            j -= 1
            unordered_list[j + 1] = nxt_element
    sorted_list = unordered_list
    return sorted_list


demo = [23, 45, 12, 31, 58, 34, 98, 65, 78]
print(insertion_sort(demo))
print(demo)
