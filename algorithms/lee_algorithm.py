"""Lee elgorithm for maze finding
"""
from typing import List, Tuple
from collections import deque


def find_path(grid: List[List[int]], start: Tuple[int, int], end: Tuple[int, int]):
    """Method to find the shortest path in a grid
    """
    rows, cols = len(grid), len(grid[0])
    dist_travalled = 0
    visited = [[False]*cols for _ in range(rows)]
    visited[0][0] = True
    queue = deque()
    queue.append(start)
    while queue:
        next_q = deque()
        while queue:
            curr_row, curr_col = queue.pop()
            if (curr_row, curr_col) == end:
                return dist_travalled
            for n_r, n_c in [(curr_row+1, curr_col), (curr_row-1, curr_col), 
                             (curr_row, curr_col+1), (curr_row, curr_col-1)]:
                if 0 <= n_r < rows and 0 <= n_c < cols and not visited[n_r][n_c]:
                    next_q.append((n_r, n_c))
                    visited[n_r][n_c] = True
        queue = next_q
        dist_travalled += 1
    return -1

if __name__=="__main__":
    matrix = [
        [1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
        [0, 1, 1, 1, 1, 1, 0, 1, 0, 1],
        [0, 0, 1, 0, 1, 1, 1, 0, 0, 1],
        [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
        [0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
        [1, 0, 1, 1, 1, 0, 0, 1, 1, 0],
        [0, 0, 0, 0, 1, 0, 0, 1, 0, 1],
        [0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
        [1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
        [0, 0, 1, 0, 0, 1, 1, 0, 0, 1]
    ]
    start = (0, 0)
    dest = (7, 5)
    print(find_path(matrix, start, dest))
