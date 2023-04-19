"""Module with demo for floyd warshall algorithm
    for all pair shortest path
"""


def get_all_pair_shortest_path(edges, vertices):
    """Method to get shortes paths for all pairs
    """
    for intermediary in range(vertices):
        for src in range(vertices):
            for dst in range(vertices):
                if edges[src][dst] > edges[src][intermediary] + edges[intermediary][dst]:
                    edges[src][dst] = edges[src][intermediary] + edges[intermediary][dst]
    return edges

if __name__=="__main__":
    INF = float("inf")
    edges = [[0, 5, INF, 10],
             [INF, 0, 3, INF],
             [INF, INF, 0,   1],
             [INF, INF, INF, 0]
             ]
    res = get_all_pair_shortest_path(edges, 4)
    for row in res:
        print(row)
