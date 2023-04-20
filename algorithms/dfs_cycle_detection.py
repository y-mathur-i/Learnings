"""Module for cycle detection via dfs in graph
"""
from collections import defaultdict
from typing import List


def detect_cycle(edges: List, nodes: int) -> bool:
    """Method to detect cycle in undirected graph
    """
    graph = defaultdict(list)
    visited = set()
    stk = [False for _ in range(nodes)]
    for src, dst in edges:
        graph[src].append(dst)
        graph[dst].append(src)
    for node in range(nodes):
        if node not in visited:
            if detect_cycle_helper(graph, node, visited, stk):
                return True
    return False

def detect_cycle_helper(graph, curr, visited, stk) -> bool:
    """helper method to detect cycle
    """
    visited.add(curr)
    stk[curr] = True
    for nei in graph[curr]:
        if nei not in visited:
            if detect_cycle_helper(graph, nei, visited, stk):
                return True
        elif stk[nei]:  # if we are still going down a path and see a node we have not finished
            return True
    stk[curr] = False
    return False

if __name__=="__main__":
    edges = [[0, 1], [0, 2], [1, 2], [2, 0], [2, 3], [3, 3]]
    nodes = 4
    print(detect_cycle(edges=edges, nodes=4))
