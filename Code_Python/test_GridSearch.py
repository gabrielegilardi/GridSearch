"""
Test file for the grid search algorithms in file <GridSearch.py>

Copyright (c) 2020 Gabriele Gilardi


There are three examples:
- Example 1 uses the grid in file <simple.txt> and solve the search problem
  using all four methods with a fixed order 4-way motion.
- Example 2 uses the grid in file <simple.txt> and solve the search problem
  using DFS with a probabilistic 4-way motion.
- Example 3 uses the grid in file <diagonal.txt> and solve the search problem
  using BFS and A* with a fixed order 8-way motion.
- Another example of grid is in file <maze.txt>.
"""

import numpy as np
from GridSearch import GridSearch

np.random.seed(1294404794)

# Directions start from North and move clockwise.
offset4 = [(-1, 0), (0, 1), (1, 0), (0, -1)]
offset8 = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

# ===== Example 1 =====
# The same grid is solved using all four methods
grid1 = GridSearch('simple.txt')
grid1.set_start(6, 2)
grid1.set_goal(2, 12)
grid1.set_motion(offset4)

# Using DFS
"""
      * * * * * * * * * * *     * * *
      * · · · · ·         * * * *   *
* * * * ·   # # · · · · G           *
*       · · · ·       * * *     * * *
* · · ·   # # ·       *   *     *
* ·   · ·     · · · · *   *     *
* · S   ·           · *   * * * *
*       · · · · · · · *
* * * * * * * * * * * *
- Steps to goal: 36
- Positions visited: 42
- Positions added: 63
"""
path = grid1.dfs()
print('\n----- Solved using DFS')
grid1.show(path)
print('- Steps to goal:', len(path)-1)
print('- Positions visited:', grid1.visited)
print('- Positions added:', grid1.added)

# Solve using BFS
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
- Positions visited: 63
- Positions added: 64
"""
path = grid1.bfs()
print('\n----- Solved using BFS')
grid1.show(path)
print('- Steps to goal:', len(path)-1)
print('- Positions visited:', grid1.visited)
print('- Positions added:', grid1.added)

# Solve using A*
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
path = grid1.A_star()
print('\n----- Solved using A*')
grid1.show(path)
print('- Steps to goal:', len(path)-1)
print('- Positions visited:', grid1.visited)
print('- Positions added:', grid1.added)

# Solve using Dijkstra's algorithm
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
- Positions visited: 63
- Positions added: 64
"""
path = grid1.Dijkstra()
print('\n----- Solved using Dijkstra algorithm')
grid1.show(path)
print('- Steps to goal:', len(path)-1)
print('- Positions visited:', grid1.visited)
print('- Positions added:', grid1.added)

# ===== Example 2 =====
# Same grid as in Example 1 solved using DFS but defining the probabilities
grid2 = GridSearch('simple.txt')
grid2.set_start(6, 2)
grid2.set_goal(2, 12)
grid2.set_motion(offset4, prob=[0.1, 0.1, 0.4, 0.4])

# Solve using DFS
"""
     * * * * * * * * * * *     * * *
      *           · · · · * * * *   *
* * * *     # #   ·     G           *
*       · · · ·   ·   * * *     * * *
*       · # # · · ·   *   *     *
*       ·             *   *     *
*   S · ·             *   * * * *
*                     *
* * * * * * * * * * * *
- Steps to goal: 18
- Positions visited: 19
- Positions added: 41
"""
path = grid2.dfs()
print('\n----- Solved using DFS')
grid2.show(path)
print('- Steps to goal:', len(path)-1)
print('- Positions visited:', grid2.visited)
print('- Positions added:', grid2.added)

# ===== Example 3 =====
# Simpler grid solved using BFS and A* with 8-way motion
grid3 = GridSearch('diagonal.txt')
grid3.set_start(11, 2)
grid3.set_goal(4, 8)
grid3.set_motion(offset8)

# Solve using BFS
"""
* * * * * * * * * * * * * * * * *
*     · · ·                     *
*   · # #   ·                   *
*   · # # #   ·                 *
*   ·   # # #   G               *
*   ·     # # #                 *
*   ·       # # #               *
*   ·         # # #             *
*   ·           # # #           *
*   ·             # # #         *
*   ·               # # #       *
*   S                 # # #     *
*                               *
* * * * * * * * * * * * * * * * *
- Steps to goal: 15
- Positions visited: 97
- Positions added: 107
"""
path = grid3.bfs()
print('\n----- Solved using BFS')
grid3.show(path)
print('- Steps to goal:', len(path)-1)
print('- Positions visited:', grid3.visited)
print('- Positions added:', grid3.added)

# Solve using A*
"""
* * * * * * * * * * * * * * * * *
*     · ·                       *
*   · # # ·                     *
*   · # # # ·                   *
*     · # # # · G               *
*       · # # #                 *
*         · # # #               *
*           · # # #             *
*         ·     # # #           *
*       ·         # # #         *
*     ·             # # #       *
*   S                 # # #     *
*                               *
* * * * * * * * * * * * * * * * *
- Steps to goal: 15
- Positions visited: 72
- Positions added: 82
"""
path = grid3.A_star()
print('\n----- Solved using A*')
grid3.show(path)
print('- Steps to goal:', len(path)-1)
print('- Positions visited:', grid3.visited)
print('- Positions added:', grid3.added)
