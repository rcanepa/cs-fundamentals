"""Given a directed graph, find the shortest path from
node start to node end."""

from heapq import heappush, heappop


def find_shortest_distance(graph, start, end):
    # (path, parent_node, current_node)
    pq = []
    heappush(pq, (0, None, start))  # (0, None, "a")

    distances = {}
    visited = {}
    hierarchy = {}
    for node in graph.keys():
        distances[node] = None
        visited[node] = False
        hierarchy[node] = None

    while pq:
        curr_distance, parent_node, current_node = heappop(pq)

        if visited[current_node]:
            continue

        visited[current_node] = True

        if not distances[current_node]:
            distances[current_node] = curr_distance
            hierarchy[current_node] = parent_node
        else:
            if curr_distance < distances[current_node]:
                distances[current_node] = curr_distance
                hierarchy[current_node] = parent_node

        for adj_node, adj_distance in graph[current_node].items():
            total_distance = curr_distance + adj_distance
            heappush(pq, (total_distance, current_node, adj_node))

    print(distances)
    print(hierarchy)

    return distances[end]


if __name__ == "__main__":
    graph = {
        "a": {
            "b": 2,
            "c": 1
        },
        "b": {
            "d": 1
        },
        "c": {
            "d": 3
        },
        "d": {
            "e": 1,
            "f": 4
        },
        "e": {
            "g": 3,
            "z": 8
        },
        "f": {
            "g": 2
        },
        "g": {
            "z": 4
        },
        "z": {}
    }
    result = find_shortest_distance(graph, "a", "z")
    print(result)
    # assert result == 11
    g = {"s": {"u": 10, "x": 5},
         "u": {"v": 1, "x": 2},
         "v": {"y": 4},
         "x": {"u": 3, "v": 9, "y": 2},
         "y": {"s": 7, "v": 6}}
    print(find_shortest_distance(g, "s", "v"))
