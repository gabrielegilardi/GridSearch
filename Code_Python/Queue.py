"""
Queue Data Structure Using Lists

Copyright (c) 2020 Gabriele Gilardi


Notes
-----
- Written and tested in Python 3.8.5.
- Queue data structure implementation using Python lists.
- The queue is from the front to the back of the list.
- Duplicate items are allowed and removed in FIFO order.
- The queue can be reversed in place.
- Examples of usage are at the end of the file.
- Reference: "Problem Solving with Algorithms and Data Structures", by Miller
  and Ranum.


Queue Class
-----------
items           List with the queue data.
size            Length of the queue.
__init__()      Initializes the priority queue.
__repr_()       Returns the string representation of the queue.
is_empty()      Checks if the queue is empty or not.
enqueue()       Adds one item to the back of the queue.
dequeue()       Returns and removes the item at the front of the queue.
peek()          Returns the item at the front of the queue.
reverse()       Reverses the queue.
clear()         Removes all items from the queue.
"""


class Queue:
    """
    Queue class using a list.
    """
    def __init__(self, init_list=None):
        """
        Initializes the queue.
        """
        # Initialize to an empty list
        if (init_list is None):
            self.items = []
            self.size = 0

        # Initialize to the initial list         
        else:
            self.items = init_list
            self.size = len(init_list)

    def __repr__(self):
        """
        Returns the string representation of the queue.
        """
        return ("{}".format(self.items))

    def is_empty(self):
        """
        Returns <True> if the queue is empty and <False> if it is not.
        """
        return not self.size

    def enqueue(self, item):
        """
        Adds one item to the back of the queue.
        """
        self.size += 1
        self.items.append(item)

    def dequeue(self):
        """
        Returns and removes the item at the front of the queue. Returns <None>
        if the list is empty.
        """
        # If the list is empty
        if (self.size == 0):
            return None

        # If the list is not empty
        else:
            self.size -= 1
            return self.items.pop(0)

    def peek(self):
        """
        Returns the item at the front of the queue without removing it. Returns
        <None> if the list is empty.
        """
        # If the list is empty
        if (self.size == 0):
            return None

        # If the list is not empty
        else:
            return self.items[0]

    def reverse(self):
        """
        Reverses (in place) the queue.
        """
        self.items.reverse()

    def clear(self):
        """
        Removes all items from the queue.
        """
        self.items.clear()
        self.size = 0


if __name__ == '__main__':
    """
    Tests the Queue class
    """
    print('\nCreate the queue with an initial list')
    queue = Queue([3, (6.4, 3.3), True, 'hello'])
    print('- queue:', queue)            # [3, (6.4, 3.3), True, 'hello']
    print('- size:', queue.size)       # 4

    print('\nClear the queue and check if empty')
    queue.clear()
    print('- queue:', queue)                    # []
    print('- empty?', queue.is_empty())         # True

    print('\nAdd items')
    queue.enqueue(3)
    queue.enqueue((6.4, 3.3))
    queue.enqueue(True)
    queue.enqueue('hello')
    print('- queue:', queue)            # [3, (6.4, 3.3), True, 'hello']

    print('\nPeek and pop the item')
    print('- item at the front:', queue.peek())     # 3
    print('- item returned:', queue.dequeue())      # 3
    print('- queue:', queue)                        # [(6.4, 3.3), True, 'hello]

    print('\nReverse, pop one item, and check if empty')
    queue.reverse()
    print('- queue:', queue)                        # ['hello', True, (6.4, 3.3)]
    print('- item returned:', queue.dequeue())      # hello
    print('- empty?', queue.is_empty())             # False

    print('\nPop all remaining items plus one')
    print('- item returned:', queue.dequeue())      # True
    print('- item returned:', queue.dequeue())      # (6.4, 3.3)
    print('- item returned:', queue.dequeue())      # None
    print('- queue:', queue)                        # []
    print('- size:', queue.size)                    # 0
