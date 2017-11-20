"""Depth First Search"""

from collections import defaultdict


def dfs(graph, vertex):
    stack = []
    visited = defaultdict(bool)
    stack.append(vertex)

    while stack:
        curr_vertex = stack.pop()
        if visited[curr_vertex]:
            print("vertex", curr_vertex, "was already visited")
            continue

        visited[curr_vertex] = True
        yield curr_vertex

        for adj_vertex in graph[curr_vertex]:
            stack.append(adj_vertex)


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

    for v in dfs(g, starting_vertex):
        print("visiting vertex = ", v)
