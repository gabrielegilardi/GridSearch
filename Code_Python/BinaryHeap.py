"""
Binary Heap Data Structure Using Lists

Copyright (c) 2020 Gabriele Gilardi


Notes
-----
- Written and tested in Python 3.8.5.
- Min/max binary heap data structure implementation using Python lists.
- The root item of the binary heap is at the front of the list.
- Duplicates items are allowed but there is no guarantee which one is returned
  first (this may be important if the item contains multiple data).
- Items can be any type as long as they are all of the same type.
- The binary heap can be reversed in place (min --> max, max --> min).
- Examples of usage are at the end of the file.
- Reference: "Problem Solving with Algorithms and Data Structures", by Miller
  and Ranum.
- find_min_max() is an helper function that returns the index of the node with
  the max/min value between the two children nodes of the same parent node.


BinaryHeap Class
----------------
heap_type       Binary heap type (min or max)
items           List with the binary heap data.
size            Length of the binary heap.
__init__()      Initializes the binary heap.
__repr_()       Returns the string representation of the binary heap.
is_empty()      Checks if the binary heap is empty or not.
swap_up()       Swaps an item up to preserve the binary heap property.
swap_down()     Swaps an item down to preserve the binary heap property.
put()           Adds one item to the binary heap.
get()           Returns and removes the item at the root of the binary heap.
peek()          Returns the item at the root of the binary heap.
reverse()       Reverses the binary heap (from min to max and viceversa).
clear()         Removes all items from the binary heap.
"""


def find_min_max(items, idx, heap_type):
    """
    Returns the index of the node with the max/min value between two children.
    """
    size = len(items) - 1
    left = 2 * idx
    right = 2 * idx + 1

    # if only one child it must be the left node
    if (right > size):
        return left

    # Check if the left node has the max/min value
    if (heap_type == 'max'):
        flag = items[left] > items[right]
    else:
        flag = items[left] < items[right]

    # Assign the index with the max/min
    ic = left if (flag) else right

    return ic


class BinaryHeap:
    """
    Binary heap class using a list.
    """
    def __init__(self, init_list=None, heap_type='min'):
        """
        Initializes the binary heap.
        """
        self.heap_type = heap_type

        # Initialize to an empty list
        if (init_list is None):

            self.items = [0]
            self.size = 0

        # Initialize to the initial list
        else:

            self.items = [0] + init_list[:]
            self.size = len(init_list)

            idx = self.size // 2
            while (idx > 0):
                self.swap_down(idx)
                idx -= 1

    def __repr__(self):
        """
        Returns the string representation of the binary heap.
        """
        return ("{}".format(self.items[1:]))

    def is_empty(self):
        """
        Returns <True> if the binary heap is empty and <False> if it is not.
        """
        return not self.size

    def swap_up(self, ic):
        """
        Swaps an item up to preserve the heap property.

        - min heap: swaps up if the content of the child node is lower then
                    the content of the parent node.
        - max heap: swaps up if the content of the child node is greater then
                    the content of the parent node.
        """
        while ((ic // 2) > 0):

            ip = ic // 2        # Index of the parent node

            # Check if the swap condition is satisfied
            if (self.heap_type == 'max'):
                swap = (self.items[ic] > self.items[ip])        # max heap
            else:
                swap = (self.items[ic] < self.items[ip])        # min heap

            # Swap the two nodes
            if (swap):
                self.items[ip], self.items[ic] = self.items[ic], self.items[ip]

            # Next parent-child pair
            ic = ip

    def swap_down(self, ip):
        """
        Swaps an item down to preserve the heap property.

        - min heap: swaps down if the content of the parent node is greater
                    then the content of the child node.
        - max heap: swaps down if the content of the parent node is lesser
                    then the content of the child node.
        """
        while ((2 * ip) <= self.size):

            # Index of the node with the max/min value between the children
            ic = find_min_max(self.items, ip, self.heap_type)

            # Check if the swap condition is satisfied
            if (self.heap_type == 'max'):
                swap = (self.items[ip] < self.items[ic])        # max heap
            else:
                swap = (self.items[ip] > self.items[ic])        # min heap

            # Swap the two nodes
            if (swap):
                self.items[ip], self.items[ic] = self.items[ic], self.items[ip]

            # Next parent-child pair
            ip = ic

    def put(self, item):
        """
        Adds one item to the heap preserving the heap property.
        """
        # Add the item at the end of the heap.
        self.items.append(item)
        self.size += 1

        # Swap up the added item
        self.swap_up(self.size)

    def get(self):
        """
        Returns and removes the item at the root of the binary heap preserving
        the heap property. Returns <None> if the list is empty.
        """
        # If the list is empty
        if (self.size == 0):
            return None

        # If the list is not empty
        else:

            # Save the item at the root
            root_item = self.items[1]

            # Move the last item in the binary heap to the root
            self.items[1] = self.items[-1]
            self.items.pop()
            self.size -= 1

            # Swap down the item at the root
            self.swap_down(1)

            return root_item

    def peek(self):
        """
        Returns the item at the root of the binary heap without removing it.
        Returns <None> if the list is empty.
        """
        # If the list is empty
        if (self.size == 0):
            return None

        # If the list is not empty
        else:
            return self.items[1]

    def reverse(self):
        """
        Reverses the binary heap (from min to max and viceversa).
        """
        self.heap_type = 'min' if (self.heap_type == 'max') else 'max'

        idx = self.size // 2
        while (idx > 0):
            self.swap_down(idx)
            idx -= 1

    def clear(self):
        """
        Removes all items from the binary heap.
        """
        self.items.clear()
        self.items = [0]
        self.size = 0


if __name__ == '__main__':
    """
    Tests the BinaryHeap class
    """
    print('\nCreate the binary heap with an initial list')
    heap = BinaryHeap([3, 8, 6, 3, 1, 0, 4, 2])
    print('- priority queue:', heap)    # [0, 1, 3, 2, 8, 6, 4, 3]
    print('- size:', heap.size)         # 8
    print('- type:', heap.heap_type)    # min

    print('\nClear the binary heap and check if empty')
    heap.clear()
    print('- binary heap:', heap)           # []
    print('- empty?', heap.is_empty())      # True

    print('\nAdd items')
    heap.put(3)
    heap.put(8)
    heap.put(6)
    heap.put(3)
    heap.put(1)
    heap.put(0)
    heap.put(4)
    heap.put(2)
    print('- binary heap:', heap)   # [0, 2, 1, 3, 3, 6, 4, 8]

    print('\nPeek and get the item')
    print('- item at the root:', heap.peek())   # 0
    print('- item returned:', heap.get())       # 0
    print('- binary heap:', heap)               # [1, 2, 4, 3, 3, 6, 8]

    print('\nReverse, get one item, and check if empty')
    heap.reverse()
    print('- binary heap:', heap)               # [8, 3, 6, 3, 2, 1, 4]
    print('- type:', heap.heap_type)            # max
    print('- item returned:', heap.get())       # 8
    print('- empty?', heap.is_empty())          # False

    print('\nGet all remaining items plus one')
    print('- item returned:', heap.get())       # 6
    print('- item returned:', heap.get())       # 4
    print('- item returned:', heap.get())       # 3
    print('- item returned:', heap.get())       # 3
    print('- item returned:', heap.get())       # 2
    print('- item returned:', heap.get())       # 1
    print('- item returned:', heap.get())       # None
    print('- binary heap:', heap)               # []
    print('- size:', heap.size)                 # 0

    print('\nExamples of string-type items')
    heap = BinaryHeap(['hello', 'world', 'car', 'house', 'me', 'funny'])
    print('- priority queue:', heap)    # ['car', 'house', 'funny', 'world', 'me', 'hello']
    heap.reverse()
    print('- binary heap:', heap)       # ['world', 'me', 'hello', 'house', 'car', 'funny']
