"""Module with dijkstra algo
    Using submission for leetcode problem
"""
from typing import List
from collections import deque, defaultdict
import heapq


def networkDelayTime(times: List[List[int]], n: int, k: int) -> int:
    inf = float("inf")
    q = deque()
    q.append((0, k))
    graph = defaultdict(list)
    for s, d, w in times:
        graph[s].append((d, w))
    heap = [(0, k)]
    dist = [inf]*(n+1)
    dist[k] = 0
    while heap:
        c_dist, curr = heapq.heappop(heap)
        for dst, w in graph[curr]:
            if dist[dst] > c_dist + w:
                dist[dst] = c_dist + w
                heapq.heappush(heap, (dist[dst], dst))
    # print(dist)
    res = max(dist[1:])
    return res if res != inf else -1
