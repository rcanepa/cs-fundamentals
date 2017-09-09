var GraphAPI = {
  vertices: 0,
  connectionMatrix: [],
  getMatrix: getMatrix,
  addEdge: addEdge,
  areConnected: areConnected,
  getNeighbors: getNeighbors
};

function getMatrix() {
  return this.connectionMatrix;
}

function addEdge(v1, v2) {
  if (v1 >= this.vertices || v2 >= this.vertices)
    throw new Error(
      "You can't connect those vertices, because at least one of them doesn't exist."
    );
  this.connectionMatrix[v1][v2] = 1;
  if (!this.directed) this.connectionMatrix[v2][v1] = 1;
}

function areConnected(v1, v2) {
  return this.connectionMatrix[v1][v2] === 1;
}

function getNeighbors(v) {
  var neighbors = [];
  for (var i = 0; i < this.vertices; i++) {
    if (this.areConnected(v, i)) {
      neighbors.push(i);
    }
  }
  return neighbors;
}

function initGraph(graph) {
  graph.connectionMatrix = [];
  var disconnetedVertices = [];
  for (var i = 0; i < graph.vertices; i++) {
    disconnetedVertices.push(0);
  }
  for (var i = 0; i < graph.vertices; i++) {
    graph.connectionMatrix.push(disconnetedVertices.slice(0, graph.vertices));
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
  initGraph(graph);
  return graph;
}

module.exports = {
  Graph
};
