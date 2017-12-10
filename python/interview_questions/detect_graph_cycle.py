"""Given a graph G, return True if the graph contain any cycle and the
cycle itself."""


def has_cycle(graph, s=0):
    stack = set()
    visited = [False] * len(graph.keys())
    cycle_detected = False
    cycle_path = []

    def _dfs(v):
        if v in stack:
            nonlocal cycle_detected
            cycle_detected = True
            path = list(stack)
            cycle_v = path.pop()
            cycle_path.append(v)
            while path and cycle_v != v:
                cycle_path.append(cycle_v)
                cycle_v = path.pop()
            cycle_path.append(v)
            return
        stack.add(v)
        for adj in graph[v]:
            if not visited[adj]:
                _dfs(adj)
        visited[v] = True
        stack.remove(v)

    _dfs(s)

    return cycle_detected, cycle_path


if __name__ == "__main__":
    test_cases = [
        (
            {
                0: [1],
                1: [2],
                2: [3],
                3: [4],
                4: [5],
                5: [2]
            },
            (True, [2, 5, 4, 3, 2])
        ),
        (
            {
                0: [1],
                1: [2, 3],
                2: [3],
                3: []
            },
            (False, [])
        )
    ]

    for input_graph, expected_result in test_cases:
        result = has_cycle(input_graph)
        print(result)
        assert result == expected_result
