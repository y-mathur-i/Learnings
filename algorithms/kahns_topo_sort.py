"""Algorithm implmentation for kahns topological sort algo
"""
from typing import List
from collections import defaultdict, deque


def perform_topo_sort(edges: List, n: int) -> List[int]:
    """Method to perform topo sort using kahn's algorithm
    """
    graph = defaultdict(list)
    in_degs = defaultdict(int)
    for src, dst in edges:
        graph[src].append(dst)
        in_degs[dst] += 1
    qu = deque()
    for node in range(n):
        if not in_degs[node]:
            qu.append(node)
    res = []
    while qu:
        curr = qu.pop()
        res.append(curr)
        for nei in graph[curr]:
            in_degs[nei] -= 1
            if not in_degs[nei]:
                qu.append(nei)
    return res if len(res) == n else -1



if __name__ == "__main__":
    edges = [[0, 1], [0, 2], [2, 1]]
    print(perform_topo_sort(edges=edges, n=3))
