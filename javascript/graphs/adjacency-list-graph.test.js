var { Graph } = require("./adjacency-list-graph");

describe("Initialization", () => {
  test("Passing undefined or less than 1 vertices should throw an error", () => {
    expect(() => Graph()).toThrow();
    expect(() => Graph(0)).toThrow();
  });

  test("The adjacency list should be initialized with empty arrays", () => {
    expect(Graph(2).getAdjacencyList()).toEqual({
      0: [],
      1: []
    });
    expect(Graph(1).getAdjacencyList()).toEqual({ 0: [] });
    expect(Graph(2).getAdjacencyList()).toEqual({
      0: [],
      1: []
    });
    expect(Graph(5).getAdjacencyList()).toEqual({
      0: [],
      1: [],
      2: [],
      3: [],
      4: []
    });
  });
});

describe("Adding and removing edges", () => {
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

    test("After removing an edge between two vertices, they shouldn't be neighbors anymore", () => {
      graph.removeEdge(0, 1);
      expect(graph.getNeighbors(0)).toEqual([3, 4]);
      expect(graph.areConnected(0, 1)).toBeFalsy();
      expect(graph.areConnected(1, 0)).toBeFalsy();
      expect(graph.getNeighbors(1)).toEqual([]);
    });
  });

  describe("Directed Graph", () => {
    var graph = Graph(10, true);
    graph.addEdge(0, 1);
    test("Edges should have a direction", () => {
      expect(graph.areConnected(0, 1)).toBeTruthy();
      expect(graph.areConnected(1, 0)).toBeFalsy();
    });

    test("Edge deletion respects direction", () => {
      graph.addEdge(1, 0);
      expect(graph.areConnected(0, 1)).toBeTruthy();
      expect(graph.areConnected(1, 0)).toBeTruthy();
      graph.removeEdge(0, 1);
      expect(graph.areConnected(0, 1)).toBeFalsy();
      expect(graph.areConnected(1, 0)).toBeTruthy();
    });
  });
});
