"""Simple bfs and dfs
"""
from collections import deque


def dfs(done: set, curr: int, graph: dict) -> None:
    """The nodes are explored by going down on each path one by one
    """
    if curr not in done:
        done.append(curr)
        for nei in graph.get(curr, []):
            dfs(done, nei, graph)


def bfs(graph: dict, start_node: int) -> None:
    """Bfs explores nodes in lvl wise method
    """
    qu = deque()
    done = []
    qu.append(start_node)
    done.append(start_node)
    while qu:
        curr = qu.pop()
        for nei in graph.get(curr, []):
            if nei not in done:
                done.append(nei)
                qu.append(nei)
    print(done)

if __name__ == "__main__":
    # Taking a small example to demonstrate the sequence followed in both algos
    graph = {0: [1, 2], 1: [3], 4: []}
    print("notice how we fo down 0 -> 1 -> 3")
    done = []
    dfs(done, 0, graph)
    print(done)
    print("observe how it goes 0 -> 1/2 -> 3")
    bfs(graph, 0)
