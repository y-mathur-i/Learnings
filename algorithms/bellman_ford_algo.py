"""Implemenmted bellman ford algo
    Reports negative cycle if there
    single source shortest path Unlike floyd .i.e all pair shortest path
"""
from typing import List

def getPath(parent, vertex):
    """Method to generaten path
    """
    if vertex < 0:
        return []
    return getPath(parent, parent[vertex]) + [vertex]


def bellman_ford(edges: List[List[int]], src: int, n: int) -> None:
    """Method relaxes edges for v times and checks if some can still
        be relaxed if yes a cycle is detected
    """
    dist = [float("inf") for _ in range(n)]
    dist[src] = 0
    parent = [-1 for _ in range(n)]
    for _ in range(n-1):
        for s, d, w in edges:
            if dist[d] > dist[s] + w:
                dist[d] = w + dist[s]
                parent[d] = s

    for s, d, w in edges:
        # still can be relaxed
        if dist[d] != float("inf") and dist[d] > dist[s] + w:
            return -1
    
    for i in range(n):
        if i != src and dist[i] < float("inf"):
            print(f'The distance of vertex {i} from vertex {src} is {dist[i]}. '
                  f'Its path is', getPath(parent, i))


if __name__ == "__main__":
    edges = [
        (0, 1, -1), (0, 2, 4), (1, 2, 3), (1, 3, 2),
        (1, 4, 2), (3, 2, 5), (3, 1, 1), (4, 3, -3)
    ]
    n = 5
    for src in range(n):
        bellman_ford(edges, src, n)

    
