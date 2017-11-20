from collections import defaultdict
from queue import PriorityQueue


def dijkstra(graph, start):
    visited = defaultdict(bool)
    shortest_distance = {}
    predecessor = {}
    pq = PriorityQueue()
    pq.put((0, start))

    while not pq.empty():
        curr_distance, curr_vertex = pq.get()
        if visited[curr_vertex]:
            break

        print("Visiting vertex", curr_vertex)
        visited[curr_vertex] = True
        neighbors = graph[curr_vertex]

        for vertex, distance in neighbors.items():
            if vertex not in shortest_distance or shortest_distance[vertex] > distance + curr_distance:
                shortest_distance[vertex] = distance + curr_distance
                predecessor[vertex] = curr_vertex
            pq.put((distance + curr_distance, vertex))

    print(shortest_distance)


if __name__ == "__main__":
    g = {"s": {"u": 10, "x": 5},
         "u": {"v": 1, "x": 2},
         "v": {"y": 4},
         "x": {"u": 3, "v": 9, "y": 2},
         "y": {"s": 7, "v": 6}}

    starting_node = "s"
    dijkstra(g, starting_node)
