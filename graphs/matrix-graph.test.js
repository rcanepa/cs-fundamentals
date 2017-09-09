var { Graph } = require("./matrix-graph");

describe("Initialization", () => {
  test("Passing undefined or less than 1 vertices should throw an error", () => {
    expect(() => Graph()).toThrow();
    expect(() => Graph(0)).toThrow();
  });
  test("The Graph should contain a matrix of size x size", () => {
    expect(Graph(1).getMatrix()).toEqual([[0]]);
    expect(Graph(2).getMatrix()).toEqual([[0, 0], [0, 0]]);
    expect(Graph(5).getMatrix()).toEqual([
      [0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0]
    ]);
  });
});

describe("Adding edges", () => {
  describe("Undirected Graph", () => {
    var graph = Graph(10);
    graph.addEdge(0, 1);
    graph.addEdge(0, 3);
    graph.addEdge(0, 4);
    graph.addEdge(2, 5);
    test("Adding an edge between vertices that don't exist should throw an error", () => {
      expect(() => graph.addEdge(0, 11)).toThrow();
    });
    test("Adding an edge between two vertices should connect them both ways", () => {
      expect(graph.areConnected(0, 1)).toBeTruthy();
      expect(graph.areConnected(1, 0)).toBeTruthy();
    });
    test("Vertices should be connected an less there is an edge between them", () => {
      expect(graph.areConnected(0, 2)).toBeFalsy();
    });
    test("Adding an edge between vertices makes them neighbors", () => {
      expect(graph.getNeighbors(0)).toEqual([1, 3, 4]);
      expect(graph.getNeighbors(2)).toEqual([5]);
    });
  });

  describe("Directed Graph", () => {
    var graph = Graph(10, true);
    graph.addEdge(0, 1);
    test("Edges should have a direction", () => {
      expect(graph.areConnected(0, 1)).toBeTruthy();
      expect(graph.areConnected(1, 0)).toBeFalsy();
    });
  });
});