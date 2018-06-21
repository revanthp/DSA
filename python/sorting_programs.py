
class MySortingAlgo():

    def __init__(self, list_):
        self.list_ = list_
        self.list_len = len(self.list_)

    def bubble_sort(self):  # O(n^2)
        """

        :param list_:
        :return:
        """
        for _ in range(self.list_len): # O(n)
            for i in range(self.list_len - 1):  # O(n)
                if self.list_[i] > self.list_[i + 1]:
                    self.list_[i], self.list_[i + 1] = self.list_[i + 1], self.list_[i]  # swap

    def selection_sort(self): # O(n^2)
        for index in range(self.list_len):  # O(n)
            min_value = min(self.list_[index:self.list_len])     # O(n - index)
            min_index = self.list_[index:self.list_len].index(min_value)
            self.list_[index], self.list_[min_index + index] = self.list_[min_index + index], self.list_[index]  # swap

    def insertion_sort(self):
        for index in range(self.list_len):
            min_value = min(self.list_[0:index])  # O(n)
            min_index = self.list_[0:index].index(min_value)
            self.list_[index], self.list_[min_index] = self.list_[min_index], self.list_[index]  # swap

    def merge_sort(self, alist):

        if len(alist) > 1:
            mid = len(alist) // 2
            lefthalf = alist[:mid]
            righthalf = alist[mid:]

            self.merge_sort(lefthalf)
            self.merge_sort(righthalf)

            i, j, k = 0, 0, 0

            while i < len(lefthalf) and j < len(righthalf):
                if lefthalf[i] < righthalf[j]:
                    alist[k] = lefthalf[i]
                    i = i + 1
                else:
                    alist[k] = righthalf[j]
                    j = j + 1
                k = k + 1

            while i < len(lefthalf):
                alist[k] = lefthalf[i]
                i, k = i + 1, k + 1

            while j < len(righthalf):
                alist[k] = righthalf[j]
                j, k = j + 1, k + 1

    def partition(alist, first, last):
        pivotvalue = alist[first]

        leftmark = first + 1
        rightmark = last

        done = False
        while not done:

            while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
                leftmark = leftmark + 1

            while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
                rightmark = rightmark - 1

            if rightmark < leftmark:
                done = True
            else:
                temp = alist[leftmark]
                alist[leftmark] = alist[rightmark]
                alist[rightmark] = temp

        temp = alist[first]
        alist[first] = alist[rightmark]
        alist[rightmark] = temp

        return rightmark

    def quick_sort_helper(self, alist, first, last):
        if first < last:
            splitpoint = self.partition(alist, first, last)

            self.quick_sort_helper(alist, first, splitpoint - 1)
            self.quick_sort_helper(alist, splitpoint + 1, last)

    def quick_sort(self, alist):
        self.quick_sort_helper(alist, 0, len(alist) - 1)


obj = MySortingAlgo([8, 10, 5, 13, 35, 27])

print(obj.list_)

obj.bubble_sort()

print(obj.list_)

