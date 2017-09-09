var { Graph } = require("./matrix-graph");

function visitVertice(graph, queue, visited, workFn) {
  while (queue.length > 0) {
    const current = queue.shift();
    const neighbors = graph.getNeighbors(current);
    visited[current] = true;
    workFn(current);

    // Add non visited neighbors to the processing queue
    for (var index = 0; index < neighbors.length; index++) {
      const neighbor = neighbors[index];
      if (!visited[neighbor] && queue.indexOf(neighbor) === -1) {
        queue.push(neighbor);
      }
    }
  }
}

function bfs(graph, workFn) {
  var queue = [];
  var visited = [];
  for (var i = 0; i < graph.vertices; i++) {
    if (!visited[i]) {
      queue.push(i);
      visitVertice(graph, queue, visited, workFn);
    }
  }
}

module.exports = {
  bfs
};

var undirectedGraph = Graph(10);
undirectedGraph.addEdge(0, 6);
undirectedGraph.addEdge(0, 2);
undirectedGraph.addEdge(0, 3);
undirectedGraph.addEdge(2, 4);
undirectedGraph.addEdge(4, 1);

/*
  ___ 6
 /
0 --- 2 --- 4 --- 1
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

bfs(undirectedGraph, v => console.log(`visiting vertice ${v}`));
