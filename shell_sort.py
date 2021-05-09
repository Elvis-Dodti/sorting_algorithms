def shell_sort(unordered_list: list):
    """
    Sorts the unordered list.

    :param unordered_list: Unsorted list to sort.
    :return: Sorted list.
    """
    gap = len(unordered_list)//2
    while gap > 0:
        for i in range(gap, len(unordered_list)):
            temp = unordered_list[i]
            j = i
            # sort the sub list for this gap.
            while j >= gap and unordered_list[j - gap] > temp:
                unordered_list[j] = unordered_list[j - gap]
                j = j - gap
            unordered_list[j] = temp
        # reduce the gap for the next element.
        gap = gap // 2


demo = [23, 45, 12, 31, 58, 34, 98, 65, 78]
shell_sort(demo)
print(demo)
