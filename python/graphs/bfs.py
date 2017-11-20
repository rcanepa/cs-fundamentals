"""Breadth First Search"""

from collections import defaultdict
from queue import Queue


def bfs(graph, vertex):
    q = Queue()
    visited = defaultdict(bool)
    q.put(vertex)

    while not q.empty():
        curr_vertex = q.get()
        if visited[curr_vertex]:
            continue
        yield curr_vertex
        visited[curr_vertex] = True
        for adj_vertex, in graph[curr_vertex]:
            q.put(adj_vertex)


if __name__ == "__main__":
    #
    #   --- a --- b -------- u --- v
    #  /               \
    # s --- x --- y --- w
    #  \
    #   --- c --- d
    #
    g = {"s": ["a", "x", "c"],
         "a": ["b"],
         "c": ["d"],
         "x": ["y"],
         "b": ["w", "u"],
         "y": ["w"],
         "w": [],
         "d": [],
         "u": ["v"],
         "v": []}

    starting_vertex = "s"

    for v in bfs(g, starting_vertex):
        print("visiting vertex = ", v)
