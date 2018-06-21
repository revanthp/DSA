

# find all pair of numbers that sum up to given value from 2 arrays.

def find_all_pairs(x, sum_):
    # worst case:
    #   O(nlogn * n)
    # space:
    #   O(1) for heap sort
    #   O(n) for merge sort

    x_sorted = sorted(x)

    left_index = 0
    right_index = len(x_sorted) - 1

    out = []

    while left_index < right_index:

        temp = x_sorted[left_index] + x_sorted[right_index]

        if temp == sum_:
            out.append((left_index, right_index))
            left_index += 1
        elif temp < sum_:
            left_index += 1
        else:
            right_index -= 1

    return out


def find_all_pairs(x, sum_):
    # time: O(n)
    # space: O(n)
    s = set()

    out = []

    for x_ in x:
        temp = sum_ - x_
        if temp >= 0 and temp in s:
            out.append((x_, temp))
        s.add(x_)
    print(s)
    return out

def find_all_pairs(x, sum_):
    s = set(x)
    out = []
    for x_ in s:
        temp = sum_ - x_
        if temp in s:
            out.append((x_, temp))
    return out



# def find_all_pairs(x, y, sum_, linear_search=False):
#     x_sorted = sorted(x)
#     y_sorted = sorted(y)
#
#     out = []
#     if linear_search:
#         for x_ in x_sorted:  # O(n^2)
#             sum_complement = sum_ - x_
#             out.extend([(x_, y_) for y_ in y_sorted if y_ == sum_complement])
#     # else:
#         # implement binary search for O(n log n)
#     return out


x = [0, 1, 5, 8, 11, 13, 13, 50]
y = [11, 22, 33, 44, 55, 66, 77]

x = [5, 3, 1, 7, 6, 2, 0, 8]

print(find_all_pairs(x, 8))








# print(find_all_pairs(x, y, 44))

# def binary_search(seq, t):
#     min = 0
#     max = len(seq) - 1
#     while True:
#         if max < min:
#             return -1
#         m = (min + max) // 2
#         if seq[m] < t:
#             min = m + 1
#         elif seq[m] > t:
#             max = m - 1
#         else:
#             return m
#
#
# print(binary_search(x, 13))

