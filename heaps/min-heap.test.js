var { MinHeap } = require("./min-heap");

describe("Inserting and removing", () => {
  var h = MinHeap();
  h
    .insert(10)
    .insert(100)
    .insert(50)
    .insert(4)
    .insert(40)
    .insert(30)
    .insert(1)
    .insert(-1);

  test("`size` should return the number of elements", () => {
    expect(h.size()).toBe(8);
  });

  test("`min` should return the smallest value without removing it", () => {
    expect(h.min()).toBe(-1);
    expect(h.size()).toBe(8);
  });

  test("`removeMin` should return and remove the smallest element", () => {
    expect(h.removeMin()).toBe(-1);
    expect(h.size()).toBe(7);
  });

  test("Removing all elements should return them in increasing order", () => {
    var elements = [];
    while (h.size() > 0) {
      elements.push(h.removeMin());
    }
    expect(elements).toEqual(elements.sort((a, b) => a - b));
    expect(h.size()).toBe(0);
  });
});
