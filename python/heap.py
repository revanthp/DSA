
# Binary Heap
# Heap rule:
#   leaf node should be greater than parent node,
#   leaf_node > parent_node


class BinaryHeap:

    def __init__(self):
        self.heaplist = [0]
        self.size = 0

    def buildHeap(self, alist):  # O(n)
        self.heaplist = alist
        self.size = len(alist)
        index = self.size // 2
        while index > 0:
            self.percolateDown(index)
            index -= 1

    def percolateUp(self, index):  # O(log n)
        while index // 2 > 0:
            if self.heaplist[index] > self.heaplist[index // 2]:  # Swap
                self.heaplist[index], self.heaplist[index // 2] = self.heaplist[index // 2], self.heaplist[index]

    def insert(self, item):  # O(log n)
        self.heaplist.append(item)
        self.size += 1
        self.percolateUp(self.size)

    def percolateDown(self, index):  # O(n)

        while (2 * index) < self.size:

            mc_index = self.minChild(index)

            if self.heaplist[index] > self.heaplist[mc_index]:  # swap
                self.heaplist[index], self.heaplist[mc_index] = self.heaplist[index], self.heaplist[index]

    def minChild(self, index):  # O(1)

        if index * 2 + 1 > self.size:  # if only one node is present
            return index * 2
        else:  # for 2 nodes
            if self.heaplist[index * 2] < self.heaplist[index * 2 + 1]:
                return index * 2  # return left leaf index
            else:
                return index * 2 + 1  # return right leaf index

    def deleteMin(self):  # O(n)
        retval = self.heaplist[1]
        self.heaplist[1] = self.heaplist[self.size]
        self.heaplist.pop()
        self.size -= 1
        self.percolateDown(1)
        return retval


