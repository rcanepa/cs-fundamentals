var GraphAPI = {
  vertices: 0,
  getAdjacencyList: getAdjacencyList,
  addEdge: addEdge,
  removeEdge: removeEdge,
  areConnected: areConnected,
  getNeighbors: getNeighbors
};

function getAdjacencyList() {
  return this.adjacencyList;
}

function addEdge(v1, v2) {
  if (v1 >= this.vertices || v2 >= this.vertices)
    throw new Error(
      "You can't connect those vertices, because at least one of them doesn't exist."
    );
  if (this.areConnected(v1, v2))
    throw new Error("Vertices are already connected.");
  this.adjacencyList[v1].push(v2);
  if (!this.directed) this.adjacencyList[v2].push(v1);
}

function removeEdge(v1, v2) {
  if (v1 >= this.vertices || v2 >= this.vertices)
    throw new Error(
      "You can't delete the edge, because at least one of vertices doesn't exist."
    );
  this.adjacencyList[v1].splice(this.adjacencyList[v1].indexOf(v2), 1);
  if (!this.directed)
    this.adjacencyList[v2].splice(this.adjacencyList[v2].indexOf(v1), 1);
}

function areConnected(v1, v2) {
  return this.adjacencyList[v1].indexOf(v2) !== -1;
}

function getNeighbors(v) {
  return this.adjacencyList[v];
}

function initGraph(graph) {
  graph.adjacencyList = {};
  for (var i = 0; i < graph.vertices; i++) {
    graph.adjacencyList[i] = [];
  }
  return graph;
}

function Graph(vertices, directed) {
  if (!vertices)
    throw new Error("You must provide the vertices the graph will contain.");
  if (vertices <= 0)
    throw new Error("You can't create a graph with less than 1 one.");
  var graph = Object.create(GraphAPI);
  graph.vertices = vertices || 0;
  graph.directed = directed || false;
  return initGraph(graph);
}

module.exports = {
  Graph
};
