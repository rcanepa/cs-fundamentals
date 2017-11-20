"""
Let's suppose that I'd like to spread a promotion message across all people
in Twitter. Assuming the ideal case, if a person tweets a message, then every
follower will re-tweet the message.

You need to find the minimum number of people to reach out (for example, who
doesn't follow anyone etc) so that your promotion message is spread out across
entire network in Twitter.

Also, we need to consider loops like, if A follows B, B follows C, C follows D,
D follows A (A -> B -> C -> D -> A) then reaching only one of them is sufficient
to spread your message.

Input: A 3x3 matrix like below. In this case, a follows b, b follows c, c follows a.
       a b c
    a  1 1 0
    b  0 1 1
    c  1 0 1

    a follows a
    a follows b
    b follows a
    b follows b
    b follows c
    c follows a
    c follows c

    c -> a -> b -> a
              b -> c

Another example:

      0, 1, 2, 3, 4, 5
 0  [[1, 1, 0, 0, 0, 0],
 1   [1, 1, 1, 0, 0, 0],
 2   [0, 0, 1, 0, 0, 0],
 3   [0, 1, 0, 1, 0, 0],
 4   [0, 0, 0, 0, 1, 1],
 5   [0, 0, 0, 0, 0, 1]]

    [i, j] = 1 i follows j
    [0, 1] = 1 means 0 follows 1
    [3, 1] = 1 means 3 follows 1

    1 -> 0
    0 -> 1 -> 2
    3 -> 1 -> 2
    4 -> 5
"""


def adjacent_nodes(graph, start):
    """Given a node `start` it returns a list which shows
    which nodes are reachable from `start`. If the list
    return by start looks like [True True False True], that means
    that nodes 0, 1 and 3 are reachable from node K.

    Time Complexity: # O(V + E), where V = number of vertices
    and E the number of edges."""
    nodes = len(graph)

    visited = [False] * nodes
    followers = [start]

    # O(V + E)
    while followers:
        current_node = followers.pop()
        if visited[current_node]:
            continue

        visited[current_node] = True

        for i in range(nodes):
            if graph[i][current_node] == 1:
                followers.append(i)

    return visited


def followers_per_node(graph):
    """Create a matrix (V*V) where in which row K shows
    all nodes that are reachable from K. If row K looks
    like [True True False True] means that nodes 0, 1
    and 3 are reachable from node K.

    Time Complexity: O(V * (V + E)) = O(V^2 + V * E), where
    V = number of vertices and E the number of edges.
    """
    nodes = len(graph)
    return [adjacent_nodes(graph, node) for node in range(nodes)]


def minimal_nodes_set(graph):
    """Return the minimal set of nodes needed to reach
    all the nodes of the graph.

    Time Complexity: O(V^2)."""
    graph_size = len(graph)
    node_followers = followers_per_node(graph)
    solution = set(range(graph_size))

    # TC: O(V^2)
    # If a node K is reachable from a node J, that means that K
    # and J are part of the same graph and that K is not part
    # of the solution.
    for node in range(graph_size):
        for comparison_node, followers in enumerate(node_followers):
            if comparison_node == node:
                continue

            if followers[node] and node in solution:
                solution.remove(node)

    return solution


if __name__ == "__main__":
    g1 = [[1, 1, 0, 0, 0, 0],
          [1, 1, 1, 0, 0, 0],
          [0, 0, 1, 0, 0, 0],
          [0, 1, 0, 1, 0, 0],
          [0, 0, 0, 0, 1, 1],
          [0, 0, 0, 0, 0, 1]]
    print(minimal_nodes_set(g1))  # => {2, 5}

    g2 = [[1, 0],
          [0, 1]]
    print(minimal_nodes_set(g2))  # => {0, 1}

    g3 = [[1, 0],
          [1, 1]]
    print(minimal_nodes_set(g3))  # => {0}
