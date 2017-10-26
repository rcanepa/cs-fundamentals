var { Graph } = require("./matrix-graph");

function visitVertice(graph, stack, visited, workFn, current) {
  const neighbors = graph.getNeighbors(current);
  stack.push(current);
  workFn(current);
  for (var n = 0; n < neighbors.length; n++) {
    var next = neighbors[n];
    if (!visited[next] && stack.indexOf(next) === -1) {
      stack.push(next);
      visitVertice(graph, stack, visited, workFn, neighbors[n]);
      visited[next] = true;
      stack.pop(next);
    }
    visited[n] = true;
  }
  visited[current] = true;
  stack.pop();
}

function dfs(graph, workFn) {
  // Initialization
  var stack = [];
  var visited = [];
  for (var i = 0; i < graph.vertices; i++) {
    visited[i] = false;
  }
  if (!workFn) workFn = () => {};

  // Loop over all vertices. We don't know if there are
  // more than one graph.
  for (var i = 0; i < graph.vertices; i++) {
    if (!visited[i]) {
      visitVertice(graph, stack, visited, workFn, i);
    }
  }
}

module.exports = {
  dfs
};

var undirectedGraph = Graph(10);
undirectedGraph.addEdge(0, 1);
undirectedGraph.addEdge(0, 2);
undirectedGraph.addEdge(0, 3);
undirectedGraph.addEdge(2, 4);
undirectedGraph.addEdge(4, 6);

/*
  ___ 1
 /
0 --- 2 --- 4 --- 6
 \
  \__ 3

*/

undirectedGraph.addEdge(5, 9);
undirectedGraph.addEdge(9, 8);
undirectedGraph.addEdge(8, 7);
undirectedGraph.addEdge(5, 9);

/*

5 --- 9 --- 8 --- 7
 \
  \__ 9
*/

dfs(undirectedGraph, v => console.log(`visiting vertice ${v}`));
