# Grid Search Algorithms

Class for two-dimensional grid search algorithms using Depth First Search (DFS), Breath First Search (BFS), A* algorithm, Dijkstra'algorithm.

## Reference

[Problem Solving with Algorithms and Data Structures](https://runestone.academy/runestone/books/published/pythonds/index.html), by Miller and Ranum.

## File

`GridSearch.py` Grid search algorithms and grid methods.

```python
"""
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
```

- DFS uses a stack as data structure (imported from *Stack.py*).
- BFS uses a queue as data structure (imported from *Queue.py*).
- A* algorithm uses a priority queue as data structure and f-values as priority (imported from *PriorityQueue.py*).
- Dijkstra's algorithm uses a binary heap as data structure and g-values as priority (imported from *BinaryHeap.py*).

## Examples and Notes

`test_GridSearch.py` is the test file for *GridSearch.py*. There are also examples of grid in *simple.txt*, *diagonal.txt*, *maze.txt*. One example of simple grid solved using A* is below:

```python
"""
      * * * * * * * * * * *     * * *
      *                   * * * *   *
* * * *     # # · · · · G           *
*   · · · · · · ·     * * *     * * *
*   ·     # #         *   *     *
*   ·                 *   *     *
*   S                 *   * * * *
*                     *
* * * * * * * * * * * *
- Steps to goal: 14
- Positions visited: 41
- Positions added: 60
"""
```

See *test_GridSearch.py* for several other examples.
