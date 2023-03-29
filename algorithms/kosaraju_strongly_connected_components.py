"""Kosaraju algorithm implementation
"""
from typing import List, Set, Dict
from collections import defaultdict


class Graph:
    """Graph class with strongly connected components finding function
    """
    def __init__(self, n_nodes: int, edges: List) -> None:
        self.graph = defaultdict(list)
        self.rev_graph = defaultdict(list)
        self.n_nodes = n_nodes
        self.__gen_graph(edges)

    def __gen_graph(self, edges: List) -> None:
        """Method to generate graph and reverse graph
        """
        for src, dst in edges:
            self.graph[src].append(dst)
            self.rev_graph[dst].append(src)

    def dfs(self, curr: int, done: Set, stk: List, graph: Dict) -> None:
        """DFS function
        """
        if curr not in done:
            done.add(curr)
            for nei in graph[curr]:
                self.dfs(nei, done, stk, graph)
            stk.append(curr)

    def get_strongly_connected_components(self) -> List[List]:
        """Method to get strongly connected components
        """
        done = set()
        stk = []
        for i in range(self.n_nodes):
            self.dfs(i, done, stk, self.graph)
        completed = set()
        components = []
        for node in stk[::-1]:
            if node not in completed:
                added = []
                self.dfs(node, completed, added, self.rev_graph)
                components.append(added)
        return components

if __name__ == "__main__":
    edges = [[1, 0], [0, 2], [2, 1], [0, 3], [3, 4]]
    graph = Graph(edges=edges, n_nodes=5)
    res = graph.get_strongly_connected_components()
    print(res)
