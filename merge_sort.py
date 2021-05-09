def merge_sort(unsorted_list: list) -> list:
    """
    Splits the list into half and then sorts it.

    :param unsorted_list: Unsorted list to sort.
    :return: Sorted list.
    """
    if len(unsorted_list) <= 1:
        return unsorted_list
    # find the middle point and divide it.
    middle = len(unsorted_list) // 2
    left_list = unsorted_list[:middle]
    right_list = unsorted_list[middle:]
    left_list = merge_sort(left_list)
    right_list = merge_sort(right_list)
    return list(merge(left_list, right_list))


def merge(left_half: list, right_half: list) -> list:
    """
    Merges the sorted lists.

    :param left_half: Left half of sorted list.
    :param right_half: Right half of sorted list.
    :return: merged sorted list.
    """
    result = []
    while len(left_half) != 0 and len(right_half) != 0:
        if left_half[0] < right_half[0]:
            result.append(left_half[0])
            left_half.remove(left_half[0])
        else:
            result.append(right_half[0])
            right_half.remove(right_half[0])
    if len(left_half) == 0:
        result = result + right_half
    else:
        result = result + left_half
    return result


demo = [23, 45, 12, 31, 58, 34, 98, 65, 78]
print(merge_sort(demo))

