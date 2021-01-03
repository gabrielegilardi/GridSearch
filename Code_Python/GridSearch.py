"""
Grid Search Algorithms (DFS, BFS, A*, Dijkstra)

Copyright (c) 2020 Gabriele Gilardi


Notes
-----
- Written and tested in Python 3.8.5.
- Two-dimensional grid search implementation using Depth First Search, Breath
  First Search, A* algorithm, and Dijkstra's algorithm.
- DFS uses a stack as data structure.
- BFS uses a queue as data structure.
- A* uses a priority queue as data structure and f-values as priority.
- Dijkstra uses a binary heap as data structure and g-values as priority.
- Any offset can be defined but only 1-step motion is allowed.
- Start and goal positions can be changed dynamically.
- Obstacles can be added/removed dynamically.
- Examples of usage are in <test_GridSearch.py>.
- Reference: "Problem Solving with Algorithms and Data Structures", by Miller
  and Ranum.


GridSearch Class
----------------
layout              List of lists with the grid layout.
bound               List of lists with the grid boundaries.
start               Tuple with the start position.
goal                Tuple with the goal position.
offset              List with the offset in each allowed direction.
prob                List with the probabilities of each direction.
__init__()          Initializes the grid object.
show()              Shows the grid layout.
is_valid()          Checks if a position is inside the grid.
set_start()         Sets the start position.
set_goal()          Sets the goal position.
add_obstacle()      Adds an obstacle to the grid.
del_obstacle()      Deletes an obstacle from the grid.
set_motion()        Sets the offset and the corresponding probabilities.
order_dir()         Defines the order in the direction of motion.
get_path()          Returns the path between the start and the goal position.
dfs()               Find the path using depth first search.
bfs()               Find the path using breath first search.
A_star()            Find the path using A* algorithm.
Dijkstra()          Find the path using Dijkstra's algorithm.
"""

import numpy as np

from Stack import Stack
from Queue import Queue
from PriorityQueue import PriorityQueue
from BinaryHeap import BinaryHeap


class GridSearch:
    """
    Class for grid search algorithms.
    """
    def __init__(self, file_name):
        """
        Initialize the grid object.
        """
        # Open and read the grid layout
        try:
            fid = open(file_name, "r")
            self.layout = [[char for char in line.strip("\n")] for line in fid]
            fid.close()

        except IOError:
            raise SystemExit("\nFile not found or problem during reading")

        # Define a list containing the positions of the the grid boundaries
        self.bound = []
        for i, row in enumerate(self.layout):
            self.bound.append([i for i, x in enumerate(row) if x == "*"])
            if (len(self.bound[i]) <= 1):
                raise SystemExit("\nThe grid bounds are not consistent.")

        # Init other attributes
        self.start = None
        self.goal = None
        self.offset = None
        self.prob = None

    def show(self, path=None):
        """
        Shows the grid layout with or without the path.
        """
        # Add the path to the layout (if given)
        if (path is not None):
            for row, col in path[1:-1]:
                self.layout[row][col] = chr(183)

        # Show the layout
        for row in self.layout:
            for char in row:
                print(char, end=' ')
            print()

        # Remove the path from the layout (if given)
        if (path is not None):
            for row, col in path[1:-1]:
                self.layout[row][col] = ' '

    def is_valid(self, row, col):
        """
        Returns <True> if (row, col) is inside the grid. Returns <False> if not.
        """
        max_rows = len(self.bound)

        # Check if <row> is a valid row
        if (row >= max_rows or row <= 0):
            return False

        # Check if <col> is correctly bounded by walls
        if (col > max(self.bound[row]) or col < min(self.bound[row])):
            return False

        # Build the column corresponding to <col> and check if it is valid
        column = []
        for i, k in enumerate(self.bound):
            if (col in k):
                column.append(i)
        if (len(column) <= 1):
            raise SystemExit("\nThe grid bounds are not consistent.")

        # Check if <row> is correctly bounded by walls
        if (row > max(column) or row < min(column)):
            return False

        # Check if the position is a wall
        if (self.layout[row][col] == '*'):
            return False

        return True

    def set_start(self, row, col):
        """
        Sets the start position.
        """
        # Check if it is inside
        if (self.is_valid(row, col)):

            # If present remove the current start position
            if (self.start is not None):
                self.layout[self.start[0]][self.start[1]] = ' '

            # Set the new start position
            self.start = (row, col)
            self.layout[row][col] = 'S'

        # Raise an error if it is outside
        else:
            raise SystemExit("\nThe start position is not valid.")

    def set_goal(self, row, col):
        """
        Sets the goal position.
        """
        # Check if it is inside
        if (self.is_valid(row, col)):

            # If present remove the current goal position
            if (self.goal is not None):
                self.layout[self.goal[0]][self.goal[1]] = ' '

            # Set the new goal position
            self.goal = (row, col)
            self.layout[row][col] = 'G'

        # Raise an error if it is outside
        else:
            raise SystemExit("\nThe goal position is not valid.")

    def add_obstacle(self, row, col):
        """
        Adds an obstacle to the grid.
        """
        # Check if it is inside and add the obstacle
        if (self.is_valid(row, col)):
            self.layout[row][col] = '#'

        # Raise an error if it is outside
        else:
            raise SystemExit("\nThe obstacle position is not valid.")

    def del_obstacle(self, row, col):
        """
        Deletes an obstacle from the grid.
        """
        # Check if it is inside and remove the obstacle
        if (self.is_valid(row, col)):
            self.layout[row][col] = ' '

        # Raise an error if it is outside
        else:
            raise SystemExit("\nthe obstacle position is not valid.")

    def set_motion(self, offset, prob=None):
        """
        Sets the offset and the corresponding probabilities.
        """
        self.offset = offset
        self.prob = prob

    def order_dir(self):
        """
        Returns the direction order using the given probabilities. If no
        probabilities, uses the same order specified as in <self.offset>.
        """
        n = len(self.offset)
        idx = np.arange(n)

        if (self.prob is not None):
            idx = np.random.choice(idx, size=n, replace=False, p=self.prob)

        return idx

    def get_path(self, previous):
        """
        Returns the path between the start and the goal position.
        """
        current = self.goal
        path = []

        # Loop until the start (its predecessor is <None>)
        while (current is not None):
            path.append(current)
            current = previous[current]

        # Reverse the order
        path.reverse()

        return path

    def dfs(self):
        """
        Returns the path from the start position to the goal position using
        depth first search (DFS). Returns <None> if no solution is found.
        """
        # Initialize the stack
        stack = Stack()

        # Add the start point to the stack
        stack.push(self.start)
        previous = {self.start: None}
        self.added = 1

        # Loop until the stack is empty
        self.visited = 0
        while (not stack.is_empty()):

            # Get the last position from the stack
            current = stack.pop()
            self.visited += 1

            # Stop if it is the goal and return the path
            if (current == self.goal):
                path = self.get_path(previous)
                return path

            # Define the order in the directions
            idx = self.order_dir()

            # Add to the stack the neighbours of the current position
            for direction in idx:

                # Offset values
                row_offset, col_offset = self.offset[direction]

                # Neighbour position
                row_neigh = current[0] + row_offset
                col_neigh = current[1] + col_offset
                neighbour = (row_neigh, col_neigh)

                # If neighbour position is valid and not in the dictionary
                if (self.layout[row_neigh][col_neigh] != '#' and
                    self.layout[row_neigh][col_neigh] != '*' and
                    neighbour not in previous):

                    # Add it to the queue
                    stack.push(neighbour)
                    previous[neighbour] = current
                    self.added += 1

        return None

    def bfs(self):
        """
        Returns the path from the start position to the goal position using
        breath first search (BFS). Returns <None> if no solution is found.
        """
        # Initialize the queue
        queue = Queue()

        # Add the start point to the queue
        queue.enqueue(self.start)
        previous = {self.start: None}
        self.added = 1

        # Loop until the queue is empty
        self.visited = 0
        while (not queue.is_empty()):

            # Get the last item from the queue
            current = queue.dequeue()
            self.visited += 1

            # Stop if it is the goal and return the path
            if (current == self.goal):
                path = self.get_path(previous)
                return path

            # Define the order in the directions
            idx = self.order_dir()

            # Add to the queue the neighbours of the current position
            for direction in idx:

                # Offset values
                row_offset, col_offset = self.offset[direction]

                # Neighbour position
                row_neigh = current[0] + row_offset
                col_neigh = current[1] + col_offset
                neighbour = (row_neigh, col_neigh)

                # If neighbour position is valid and not in the dictionary
                if (self.layout[row_neigh][col_neigh] != '#' and
                    self.layout[row_neigh][col_neigh] != '*' and
                    neighbour not in previous):

                    # Add it to the queue
                    queue.enqueue(neighbour)
                    previous[neighbour] = current
                    self.added += 1

        return None

    def A_star(self):
        """
        Returns the path from the start position to the goal position using the
        A-star (A*) algorithm. Returns <None> if no solution is found.
        """

        # Heuristic distance between two positions
        def heuristic(a, b):
            """
            Calculates the Manhattan distance between two positions.
            """
            x1, y1 = a
            x2, y2 = b
            dist = abs(x1 - x2) + abs(y1 - y2)

            return dist

        # Initialize the priority queue
        pq = PriorityQueue(queue_type='min')

        # Values for the start point
        g = 0
        h = heuristic(self.goal, self.start)
        f = g + h

        # Add the start point to the priority queue.
        pq.put(f, self.start)
        g_values = {self.start: g}
        previous = {self.start: None}
        self.added = 1

        # Loop until the priority queue is empty
        self.visited = 0
        while (not pq.is_empty()):

            # Get the highest priority position from the priority queue
            f, current = pq.get()
            self.visited += 1

            # Stop if it is the goal and return the path
            if (current == self.goal):
                path = self.get_path(previous)
                return path

            # Define the order in the directions
            idx = self.order_dir()

            # Add to the priority queue the neighbours of the current position
            for direction in idx:

                # Offset values
                row_offset, col_offset = self.offset[direction]

                # Neighbour position
                row_neigh = current[0] + row_offset
                col_neigh = current[1] + col_offset
                neighbour = (row_neigh, col_neigh)

                # If neighbour position is valid and not in the dictionary
                if (self.layout[row_neigh][col_neigh] != '#' and
                    self.layout[row_neigh][col_neigh] != '*' and
                    neighbour not in previous):

                    # Values (the g-value of all neighbour positions differ
                    # from the g-value of the current position by 1)
                    g = g_values[current] + 1
                    h = heuristic(self.goal, neighbour)
                    f = g + h

                    # Add it to the priority queue
                    pq.put(f, neighbour)
                    g_values[neighbour] = g
                    previous[neighbour] = current
                    self.added += 1

        return None

    def Dijkstra(self):
        """
        Returns the path from the start position to the goal position using
        Dijkstra's algorithm (DA). Returns <None> if no solution is found.
        """

        # Initialize the binary heap
        bh = BinaryHeap(heap_type='min')

        # Add the start point to the binary heap.
        g = 0
        bh.put((g, self.start))
        g_values = {self.start: g}
        previous = {self.start: None}
        self.added = 1

        # Loop until the priority queue is empty
        self.visited = 0
        while (not bh.is_empty()):

            # Get the highest priority position from the priority queue
            (g, current) = bh.get()
            self.visited += 1

            # Stop if it is the goal and return the path
            if (current == self.goal):
                path = self.get_path(previous)
                return path

            # Define the order in the directions
            idx = self.order_dir()

            # Add to the binary heap the neighbours of the current position
            for direction in idx:

                # Offset values
                row_offset, col_offset = self.offset[direction]

                # Neighbour position
                row_neigh = current[0] + row_offset
                col_neigh = current[1] + col_offset
                neighbour = (row_neigh, col_neigh)

                # If neighbour position is valid and not in the dictionary
                if (self.layout[row_neigh][col_neigh] != '#' and
                    self.layout[row_neigh][col_neigh] != '*' and
                    neighbour not in previous):

                    # Values (the g-value of all neighbour positions differ
                    # from the g-value of the current position by 1)
                    g = g_values[current] + 1

                    # Add it to the priority queue
                    bh.put((g, neighbour))
                    g_values[neighbour] = g
                    previous[neighbour] = current
                    self.added += 1

        return None
