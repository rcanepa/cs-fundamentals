var { MinHeap } = require("./min-heap");

describe("Initialization", () => {
  var initialData = [50, 20, 100, 200, 10, 1, 8, 0, -10];
  var h = MinHeap([50, 20, 100, 200, 10, 1, 8, 0, -10]);
  test("After the initialization with an array, the Heap should reflect the correct size", () => {
    expect(h.size()).toBe(initialData.length);
  });

  test("Trying to initialize a Heap with anything different than an array, should throw an Error", () => {
    expect(() => MinHeap("abc")).toThrow();
    expect(() => MinHeap(1)).toThrow();
    expect(() => MinHeap({})).toThrow();
  });
});

describe("Inserting and removing", () => {
  var h = MinHeap();
  h
    .insert(10)
    .insert(100)
    .insert(50)
    .insert(-4)
    .insert(40)
    .insert(30)
    .insert(1)
    .insert(-1);

  test("`size` should return the number of elements", () => {
    expect(h.size()).toBe(8);
  });

  test("`min` should return the smallest value without removing it", () => {
    expect(h.min()).toBe(-4);
    expect(h.size()).toBe(8);
  });

  test("`removeMin` should return and remove the smallest element", () => {
    expect(h.removeMin()).toBe(-4);
    expect(h.size()).toBe(7);
  });

  test("Removing all elements should return them in increasing order", () => {
    var elements = [];
    var sortedElements = [];
    while (h.size() > 0) {
      elements.push(h.removeMin());
    }
    sortedElements = elements.slice(0).sort((a, b) => a - b);
    expect(elements).toEqual(sortedElements);
    expect(h.size()).toBe(0);
  });
});

describe("Merging Heaps", () => {
  var h1Data = [40, 50, 20];
  var h2Data = [10, 500, 30, 80];
  var h1 = MinHeap(h1Data);
  var h2 = MinHeap(h2Data);
  var mergedHeap = h1.merge(h2);
  test("The size of the new Heap should be the sum of the other 2", () => {
    expect(mergedHeap.size()).toBe(h1.size() + h2.size());
  });

  test("The merged Heaps should remain untouched", () => {
    expect(h1.size()).toBe(h1Data.length);
    expect(h2.size()).toBe(h2Data.length);
  });
});
