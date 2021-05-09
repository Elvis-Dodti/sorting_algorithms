def bubble_sort(unsorted_list):
    """
    Sorts the unordered list/array.

    :param unsorted_list: Unsorted list to sort.
    :return: sorted list.
    """
    # swapping elements to arrange in order
    for iter_num in range(len(unsorted_list) - 1, 0, -1):
        for index in range(iter_num):
            if unsorted_list[index] > unsorted_list[index+1]:
                temp = unsorted_list[index]
                unsorted_list[index] = unsorted_list[index + 1]
                unsorted_list[index + 1] = temp

    sorted_list = unsorted_list
    return sorted_list


if __name__ == "__main__":
    demo = [23, 45, 12, 31, 58, 34, 98, 65, 78]
    bubble_sort(demo)
    print(demo)
