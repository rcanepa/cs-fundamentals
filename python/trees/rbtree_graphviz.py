"""rbtree_graphviz.py - create a graphviz representation of a LLRBT.

The purpose of this module is to visually show how the shape of a LLRBT
changes when keys are inserted in it. For every insert, sub graph (tree)
is added to the main graph.

`initialization_list` holds the values that are inserted in the tree.
This list can be changed for a list of anything that can be compared
with > == <. For example, with `initialization_list = range(50)` keys
from 0 to 49 will be inserted in the tree.

Consider that for every key, a graph is going to be generated.
"""
from graphviz import Digraph
from trees.rbtree import LLRBT, is_red

NODE_SHAPE = "circle"
NONE_NODE_SHAPE = "point"
TITLE_SHAPE = "box"
RED_COLOR = "#b8000f"

DEFAULT_GRAPH_NODE_ATTR = {
    "shape": NODE_SHAPE,
    "color": "black",
    "style": "filled",
    "fillcolor": "#cfd3d6",
}

DEFAULT_GRAPH_EDGE_ATTR = {
    "color": "black",
    "arrowhead": "vee",
    "style": "solid",
}


def add_node(graph, node):
    """Add `node` to `graph`. `node` is a tuple with the
    following shape:
        (node_id, {<node attributes>}, {<graph's node attributes>})
            ^              ^                      ^
         string           see graphviz documentation"""
    node_id, node_attr, graph_node_attr = node
    if graph_node_attr:
        graph.attr("node", **graph_node_attr)
    graph.node(node_id, **node_attr)
    graph.attr("node", **DEFAULT_GRAPH_NODE_ATTR)
    return graph


def add_edge(graph, edge):
    """Add edge from `edge[0]` to `edge[1]` to `graph`. `edge` is
    a tuple with the following shape:
    (source_node_id, destiny_node_id, {<graph's edge attributes>})
            ^              ^                      ^
         string          string        see graphviz documentation"""
    source_node_id, destiny_node_id, graph_edge_attr = edge
    graph.attr("edge", **graph_edge_attr)
    graph.edge(source_node_id, destiny_node_id)
    graph.attr("edge", **DEFAULT_GRAPH_EDGE_ATTR)
    return graph


def generate_graph(tree, initialization_list, format="pdf"):
    if initialization_list is None or len(initialization_list) == 0:
        raise Exception("You can't generate a graph with an empty tree.")

    if not isinstance(tree, LLRBT):
        raise Exception("You need to provide an instance of a Leaf Leaning Red Black Tree (LLRBT).")

    for value in initialization_list:
        tree.insert(value)

    graph = Digraph(format="pdf",
                    node_attr=DEFAULT_GRAPH_NODE_ATTR,
                    edge_attr=DEFAULT_GRAPH_EDGE_ATTR)

    # Iterate over all keys and create nodes and edges.
    for idx, node in enumerate(tree.pre_order_traversal()):
        node_id = str(node.value)
        node_label = str(node.value)
        add_node(graph, (node_id, {"label": node_label}, {}))

        # Create edge between node and its left child.
        if node.left:
            node_left_id = str(node.left.value)

            # Paint edge red if the left child is red.
            if is_red(node.left):
                add_edge(graph, (node_id, node_left_id, {"color": RED_COLOR}))

            else:
                add_edge(graph, (node_id, node_left_id, {"color": "black"}))

        # Node doesn't have a left child so we put a dot in its place.
        else:
            null_node_value = "left-null-" + str(idx)
            add_node(graph, (null_node_value, {}, {"shape": NONE_NODE_SHAPE}))
            add_edge(graph, (node_id, null_node_value, {"color": "black"}))

        # Create edge between node and its right child.
        if node.right:
            node_right_id = str(node.right.value)

            # Paint edge red if the right child is red.
            if is_red(node.right):
                add_edge(graph, (node_id, node_right_id, {"color": RED_COLOR}))
            else:
                add_edge(graph, (node_id, node_right_id, {"color": "black"}))

        # Node doesn't have a left child so we put a dot in its place.
        else:
            null_node_value = "right-null-" + str(idx)
            add_node(graph, (null_node_value, {}, {"shape": NONE_NODE_SHAPE}))
            add_edge(graph, (node_id, null_node_value, {"color": "black"}))

    return graph


def generate_graph_per_insert(tree, initialization_list, format="pdf"):
    if initialization_list is None or len(initialization_list) == 0:
        raise Exception("You can't generate a graph with an empty tree.")

    if not isinstance(tree, LLRBT):
        raise Exception("You need to provide an instance of a Leaf Leaning Red Black Tree (LLRBT).")

    main_graph = Digraph(format=format,
                         node_attr=DEFAULT_GRAPH_NODE_ATTR,
                         edge_attr=DEFAULT_GRAPH_EDGE_ATTR)
    main_graph.attr(rankdir='LR')  # print sub graph from top to bottom

    # For every key to be inserted, create a sub graph representing
    # the tree after the insertion.
    for graph_number, value in enumerate(initialization_list):
        tree.insert(value)

        # Create sub graph.
        sub_graph_name = "cluster_" + str(graph_number)
        with main_graph.subgraph(name=sub_graph_name) as sub_graph:
            sub_graph.attr(label="Inserting = " + str(value), fontsize="12")

            # Iterate over all keys and fill the sub graph.
            for idx, node in enumerate(tree.pre_order_traversal()):
                node_id = str(graph_number) + "." + str(node.value)
                node_label = str(node.value)
                add_node(sub_graph, (node_id, {"label": node_label}, {}))

                # Create edge between node and its left child.
                if node.left:
                    node_left_id = str(graph_number) + "." + str(node.left.value)

                    # Paint edge red if the left child is red.
                    if is_red(node.left):
                        add_edge(sub_graph, (node_id, node_left_id, {"color": RED_COLOR}))

                    else:
                        add_edge(sub_graph, (node_id, node_left_id, {"color": "black"}))

                # Node doesn't have a left child so we put a dot in its place.
                else:
                    null_node_id = str(graph_number) + "-left-null-" + str(idx)
                    add_node(sub_graph, (null_node_id, {}, {"shape": NONE_NODE_SHAPE}))
                    add_edge(sub_graph, (node_id, null_node_id, {"color": "black"}))

                # Create edge between node and its right child.
                if node.right:
                    node_right_id = str(graph_number) + "." + str(node.right.value)

                    # Paint edge red if the right child is red.
                    if is_red(node.right):
                        add_edge(sub_graph, (node_id, node_right_id, {"color": RED_COLOR}))
                    else:
                        add_edge(sub_graph, (node_id, node_right_id, {"color": "black"}))

                # Node doesn't have a left child so we put a dot in its place.
                else:
                    null_node_id = str(graph_number) + "-right-null-" + str(idx)
                    add_node(sub_graph, (null_node_id, {}, {"shape": NONE_NODE_SHAPE}))
                    add_edge(sub_graph, (node_id, null_node_id, {"color": "black"}))

    return main_graph


if __name__ == "__main__":
    initialization_list = ["Z", "W", "F", "D", "S", "E", "A", "R", "C", "H", "X", "M", "P", "L"]
    # initialization_list = ["A", "B", "C", "D"]
    tree = LLRBT()
    # graph = generate_graph(tree, initialization_list)
    graph = generate_graph_per_insert(tree, initialization_list)
    graph.render("trees/rbtree.gv", view=True)

