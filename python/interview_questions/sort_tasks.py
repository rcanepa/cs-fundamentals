"""Given a lists of tasks and the dependencies between them, return
a list of sorted tasks according to the order they should be executed
given their dependencies.

Examples:
    t = {
        "t1": ["t2", "t3"],
        "t2": [],
        "t3": ["t4"],
        "t4": []
    }
    returns: ["t4", "t3", "t2", "t1"]
"""


def reachable_vertices(tasks, v):
    """TC: O(V + E), where V = len(tasks.keys()) and E is the number of edges
    between vertices."""
    visited = [False] * len(tasks.keys())
    stack = [v]
    while stack:
        curr_v = stack.pop()
        if visited[curr_v]:
            continue

        visited[curr_v] = True
        stack += tasks[curr_v]
    return visited


def topological_sort(tasks, s):
    """Perform a variant of DFS in order to find the topological
    sort starting from vertex s."""
    visited = [False] * len(tasks.keys())
    ts = []

    def _dfs(v):
        for dependency in tasks[v]:
            if not visited[dependency]:
                _dfs(dependency)
        visited[v] = True
        ts.append(v)

    _dfs(s)

    return ts


def sort_tasks(tasks):
    # Find strongly connected components (we don't know if there are
    # separated tasks graphs)
    scc = {}

    # TC: O(V * (V + E)) = O(V**2 + V * E)
    for v in tasks.keys():
        scc[v] = reachable_vertices(tasks, v)

    # O(V**2), where V = len(tasks.keys())
    starting_v = {v for v in tasks.keys()}
    for v in tasks.keys():
        for scc_starting_v, v_reach in scc.items():
            if v != scc_starting_v:
                if v_reach[v] and v in starting_v:
                    starting_v.remove(v)

    # Do a topological sort on each graph (starting_v vertices)
    results = []
    for v in starting_v:
        results.append(topological_sort(tasks, v))

    return results


if __name__ == "__main__":
    test_cases = [
        (
            {
                0: [1, 2],
                1: [3],
                2: [5, 6],
                3: [4],
                4: [9],
                5: [3],
                6: [7],
                7: [8],
                8: [4],
                9: []
            },
            [[9, 4, 3, 1, 5, 8, 7, 6, 2, 0]]
        ),
        (
            {
                0: [1, 2],
                1: [],
                2: [3],
                3: []
            },
            [[1, 3, 2, 0]]
        ),
        (
            {
                0: [1, 2],
                1: [],
                2: [3],
                3: [],
                4: [5],
                5: [6],
                6: []
            },
            [[1, 3, 2, 0], [6, 5, 4]]
        )
    ]
    for input_graph, expected_sort in test_cases:
        result = sort_tasks(input_graph)
        print(result)
        assert result == expected_sort
