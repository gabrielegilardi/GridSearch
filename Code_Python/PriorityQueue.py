"""
Priority Queue Data Structure Using Lists

Copyright (c) 2020 Gabriele Gilardi


Notes
-----
- Written and tested in Python 3.8.5.
- Min/max priority queue data structure implementation using Python lists.
- Priority data must be a number.
- The priority queue is always ordered (min --> ascending, max --> descending)
  from the front to the back of the list.
- Items with equal priority are allowed and removed in FIFO order.
- The priority queue can be reversed in place (min --> max, max --> min).
- Two dummy items (with priority -inf and +inf) are automatically added when
  the priority queue is initialized to simplify the binary search.
- Examples of usage are at the end of the file.
- Reference: "Problem Solving with Algorithms and Data Structures", by Miller
  and Ranum.


PriorityQueue Class
-------------------
queue_type      Priority queue type (min or max).
items           List with the priority queue data.
size            Length of the priority queue.
__init__()      Initializes the priority queue.
__repr_()       Returns the string representation of the priority queue.
is_empty()      Checks if the priority queue is empty or not.
put()           Adds one item to the priority queue.
get()           Returns and removes the item at the front of the priority queue.
peek()          Returns the item at the front of the priority queue.
reverse()       Reverses the priority queue (from min to max and viceversa).
clear()         Removes all items from the priority queue.
"""


from math import inf

class PriorityQueue:
    """
    Priority queue class using a list.

    - Two dummy items are added automatically to simplify the binary search.
    """
    def __init__(self, init_list=None, queue_type='min'):
        """
        Initializes the priority queue.
        """
        self.queue_type = queue_type

        # Initialize to an empty list
        self.items = [(-inf, 'dummy'), (inf, 'dummy')]
        if (self.queue_type == 'max'):
            self.items.reverse()
        self.size = 0

        # Initialize to the initial list
        if (init_list is not None):
            for priority, item in init_list:
                self.put(priority, item)

    def __repr__(self):
        """
        Returns the string representation of the priority queue.
        """
        return ("{}".format(self.items[1:-1]))

    def is_empty(self):
        """
        Returns <True> if the priority queue is empty and <False> if it is not.
        """
        return not self.size

    def put(self, priority, item):
        """
        Adds one item to the priority queue keeping the priority order.

        - If min: from the lower to the higher number.
        - if max: from the higher to the lower number.
        """
        # For any other position in the priority queue use binary search
        left = 0
        right = self.size + 1

        # Loop until left with two consecutive items
        while (right > (left + 1)):

            middle = (left + right) // 2
            p = self.items[middle][0]

            # Check if the left index needs to be moved
            if (self.queue_type == 'max'):
                flag = priority <= p
            else:
                flag = priority >= p

            # Move the left/right index
            if (flag):
                left = middle           # It is in the right side
            else:
                right = middle          # It is in the left side

        # Insert the item between <left> and <right>
        self.items.insert(right, (priority, item))

        # Increase the priority queue size
        self.size += 1

    def get(self):
        """
        Returns and removes the item with the highest priority (the one at the
        front of the priority queue). Returns <None> if the list is empty.
        """
        # If the list is empty
        if (self.size == 0):
            return None

        # If the list is not empty
        else:
            self.size -= 1
            return self.items.pop(1)

    def peek(self):
        """
        Returns the item with the highest priority (the one at the front of
        the priority queue) without removing it. Returns <None> if the list
        is empty.
        """
        # If the list is empty
        if (self.size == 0):
            return None

        # If the list is not empty
        else:
            return self.items[1]

    def reverse(self):
        """
        Reverses the priority queue (from min to max type and viceversa).
        """
        self.queue_type = 'min' if (self.queue_type == 'max') else 'max'
        self.items.reverse()

    def clear(self):
        """
        Removes all items from the priority queue.
        """
        self.items.clear()
        self.items = [(-inf, 'dummy'), (inf, 'dummy')]
        if (self.queue_type == 'max'):
            self.items.reverse()
        self.size = 0


if __name__ == '__main__':
    """
    Tests the PriorityQueue class
    """
    print('\nCreate the priority queue with an initial list')
    queue = PriorityQueue([(3, 8), (6.4, 3.3), (1.1, True), (4, 'hello')], 'max')
    print('- priority queue:', queue)   # [(6.4, 3.3), (4, 'hello'), (3, 8), (1.1, True)]
    print('- size:', queue.size)        # 4
    print('- type:', queue.queue_type)  # max

    print('\nClear the priority queue and check if empty')
    queue.clear()
    print('- priority queue:', queue)           # []
    print('- empty?', queue.is_empty())         # True

    print('\nAdd items')
    queue.put(3, 8)
    queue.put(6.4, 3.3)
    queue.put(1.1, True)
    queue.put(4, 'hello')
    print('- priority queue:', queue)   # [(6.4, 3.3), (4, 'hello'), (3, 8), (1.1, True)]

    print('\nPeek and get the item')
    print('- item at the front:', queue.peek())     # (6.4, 3.3)
    print('- item returned:', queue.get())          # (6.4, 3.3)
    print('- priority queue:', queue)               # [(4, 'hello'), (3, 8), (1.1, True)]

    print('\nReverse, get one item, and check if empty')
    queue.reverse()
    print('- priority queue:', queue)           # [(1.1, True), (3, 8), (4, 'hello')]
    print('- type:', queue.queue_type)          # min
    print('- item returned:', queue.get())      # (1.1, True)
    print('- empty?', queue.is_empty())         # False

    print('\nGet all remaining items plus one')
    print('- item returned:', queue.get())      # (3, 8)
    print('- item returned:', queue.get())      # (4, 'hello')
    print('- item returned:', queue.get())      # None
    print('- priority queue:', queue)           # []
    print('- size:', queue.size)                # 0

    print('\nExample of items with same priority')
    queue.put(3, 8)
    queue.put(6.4, 3.3)
    queue.put(1.1, True)
    queue.put(4, 'hello')
    queue.put(3, '2nd with 3')
    queue.put(3, '3rd with 3')
    print('- priority queue:', queue)   # [(1.1, True), (3, 8), (3, '2nd with 3'), (3, '3rd with 3'), (4, 'hello'), (6.4, 3.3)]
