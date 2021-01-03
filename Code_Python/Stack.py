"""
Stack Data Structure Using Lists

Copyright (c) 2020 Gabriele Gilardi


Notes
-----
- Written and tested in Python 3.8.5.
- Stack data structure implementation using Python lists.
- The stack top is at the back of the list.
- Duplicate items are allowed and removed in LIFO order.
- The stack can be reversed in place.
- Examples of usage are at the end of the file.
- Reference: "Problem Solving with Algorithms and Data Structures", by Miller
  and Ranum.


Stack Class
-----------
items           List with the stack data.
size            Length of the stack.
__init__()      Initializes the stack.
__repr_()       Returns the string representation of the stack.
is_empty()      Checks if the stack is empty or not.
push()          Adds one item to the top of the stack.
pop()           Returns and removes the item at the top of the stack.
peek()          Returns the item at the top of the stack.
reverse()       Reverses the stack.
clear()         Removes all items from the stack.
"""


class Stack:
    """
    Stack class using a list.
    """
    def __init__(self, init_list=None):
        """
        Initializes the stack.
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
        Returns the string representation of the stack.
        """
        return ("{}".format(self.items))

    def is_empty(self):
        """
        Returns <True> if the stack is empty and <False> if it is not.
        """
        return not self.size

    def push(self, item):
        """
        Adds one item to the top of the stack.
        """
        self.size += 1
        self.items.append(item)

    def pop(self):
        """
        Returns and removes the item at the top of the stack. Returns <None>
        if the list is empty.
        """
        # If the list is empty
        if (self.size == 0):
            return None

        # If the list is not empty
        else:
            self.size -= 1
            return self.items.pop()

    def peek(self):
        """
        Returns the item at the top of the stack without removing it. Returns
        <None> if the list is empty.
        """
        # If the list is empty
        if (self.size == 0):
            return None

        # If the list is not empty
        else:
            return self.items[-1]

    def reverse(self):
        """
        Reverses (in place) the stack.
        """
        self.items.reverse()

    def clear(self):
        """
        Removes all items from the stack.
        """
        self.items.clear()
        self.size = 0


if __name__ == '__main__':
    """
    Tests the Stack class.
    """
    print('\nCreate the stack with an initial list')
    stack = Stack([3, (6.4, 3.3), True, 'hello'])
    print('- stack:', stack)            # [3, (6.4, 3.3), True, 'hello']
    print('- size:', stack.size)        # 4

    print('\nClear the stack and check if empty')
    stack.clear()
    print('- stack:', stack)                    # []
    print('- empty?', stack.is_empty())         # True

    print('\nAdd items')
    stack.push(3)
    stack.push((6.4, 3.3))
    stack.push(True)
    stack.push('hello')
    print('- stack:', stack)            # [3, (6.4, 3.3), True, 'hello']

    print('\nPeek and pop the item')
    print('- item at the top:', stack.peek())       # hello
    print('- item returned:', stack.pop())          # hello
    print('- stack:', stack)                        # [3, (6.4, 3.3), True]

    print('\nReverse, pop one item, and check if empty')
    stack.reverse()
    print('- stack:', stack)                    # [True, (6.4, 3.3), 3]
    print('- item returned:', stack.pop())      # 3
    print('- empty?', stack.is_empty())         # False

    print('\nPop all remaining items plus one')
    print('- item returned:', stack.pop())      # (6.4, 3.3)
    print('- item returned:', stack.pop())      # True
    print('- item returned:', stack.pop())      # None
    print('- stack:', stack)                    # []
    print('- size:', stack.size)                # 0
