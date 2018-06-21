"""
Return all indexes for matching term.

"""


def linear_search(arr, search_elem):  # O(n)
    index_list = []

    for index in range(0, len(arr)):
        if search_elem == arr[index]:
            index_list.append(index)

    return index_list


def binary_search(alist, item):  # O(log n)

    alist.sort()

    first_index = 0
    last_index = len(alist) - 1

    found = False
    # indexes = []

    while first_index <= last_index and not found:

        midpoint = (first_index + last_index) // 2

        if item == alist[midpoint]:
            # indexes.append(midpoint)
            found = True
            return found

        elif item > alist[midpoint]:
            first_index = midpoint + 1

        elif item < alist[midpoint]:
            last_index = midpoint - 1

    return found


x = [1, 4, 2, 6, 4, 9, 10, 20, 15, 4]

print(linear_search(x, 4))  # [1, 4, 9]

print(binary_search(x, 4))


