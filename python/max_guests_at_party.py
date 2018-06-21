"""
Problem can be formulated as:
    1. Maximum guests at a party
    2. Maximum overlapping intervals
    3. Maximum overlapping line segments
"""


def get_max_overalap(start, end):
    """
    This program does not create a single array of all times with arrivals and departures.
    Instead it works similar to merge sort.
    time: O(n log n) | O(n) while loop & O(log n) for sorting.
    space: O(1)

    :param start: list with starting time/segment
    :param end: list with ending time/segment
    :return: max overlap at times/segment end points and location for max overlap.
    """

    start.sort()  # time: O(log n)
    end.sort()

    guests_in = 0
    max_guests = 0
    max_guests_at = -1

    i = j = 0

    n = len(start)

    while i < n and j < n:  # time: O(n)

        if start[i] <= end[j]:
            guests_in += 1

            if guests_in > max_guests:
                max_guests = guests_in
                max_guests_at = start[i]

            i += 1

        else:
            guests_in -= 1
            j += 1

    return [max_guests, max_guests_at]


def max_overlap(start, end):
    """
    time: O(n)
    space: O(n) | since we are creating an auxiliary list. This is actually greater than n. It should be max(start, end)

    :param start:
    :param end:
    :return:
    """

    # Create an auxiliary array to hold number of guests at each moment
    aux = (max(max(start), max(end)) + 2) * [0]

    for i in range(len(start)):
        aux[start[i]] += 1
        aux[end[i] + 1] -= 1

    rolling_sum = 0
    max_guests = 0
    max_guests_at = -1

    for i in range(len(aux)):
        rolling_sum += aux[i]

        if rolling_sum > max_guests:
            max_guests = rolling_sum
            max_guests_at = i

    return [max_guests, max_guests_at]


arr = [1, 2, 10, 5, 5]
dep = [4, 5, 12, 9, 12]

print(get_max_overalap(arr, dep))  # 3
print(max_overlap(arr, dep))







