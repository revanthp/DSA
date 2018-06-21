

"""
Sorting a linked list.

Eg:
1. 12->NULL
2. 12->56->NULL
3. 12->56->48->NULL
4. 12->56->48->21->NULL
head            tail
first element   last element

When scanning or transversing a liked list, we move from head to tail or first element to last element

Advantages of Linked list:
1. No need to preallocate memory as in arrays. Saves memory when size of data is unknown or changing.
2. Listed list can be stored anywhere in memory, unlike an array which need to be stored sequentially.

Disadvantages of Linked list:
1. Linear time scan/search. O(n). With arrays we can do O(1)
"""


class Node:

    def __init__(self, item):
        self.value = item
        self.next = None

    def transverse(self):
        """
        transverse the linked list and prints output to console.
        :return: None
        """
        node = self  # look at head node
        while node is not None:
            print(node.value)  # do something with node
            node = node.next  # Move to next node


class DualNode:

    def __init__(self, item):
        self.value = item
        self.next = None
        self.prev = None


class LinkedList:

    def __init__(self):
        self.head = None

    def new_node(self, node):
        self.head = node.next


# Working with nodes

node1 = Node(12)
node2 = Node(56)
node3 = Node(48)
node4 = Node(12)

node1.next = node2  # 12->56->NULL
node2.next = node3  # 12->56->48->NULL
node3.next = node4  # 12->56->48->12->NULL



