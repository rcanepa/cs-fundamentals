const { BSTree } = require("./binary-search-tree");

describe("Creation", () => {
  test("The size of a empty BST should be 0", () => {
    expect(BSTree().size).toBe(0);
  });
  test("The size of an initialized BST should be 1", () => {
    expect(BSTree(100).size).toBe(1);
  });
});

describe("Insertion", () => {
  var tree = BSTree();
  tree.insert(20);
  tree.insert(30);
  tree.insert(10);
  tree.insert(12);
  tree.insert(5);
  test("The tree should have the correct size", () => {
    expect(tree.size).toBe(5);
  });
});

describe("Deletion", () => {
  /**
   *         20
   *     10      30
   *    5  15  25  35
   */
  var tree = BSTree();
  var values = [20, 10, 30, 15, 5, 25, 35];
  values.forEach(v => {
    tree.insert(v);
  });
  test("Deleting the min element should reduce the size of the tree by one", () => {
    tree.deleteMin();
    /**
    *         20
    *     10      30
    *    X  15  25  35
    */
    expect(tree.size).toBe(6);
  });
  test("The min value shouldn't be present in the tree", () => {
    var remainingValues = [];
    tree.inOrderTraversal(v => remainingValues.push(v));
    expect(remainingValues.indexOf(5)).toBe(-1);
  });
  test("Deleting the max element should reduce the size of the tree by one", () => {
    tree.deleteMax();
    /**
    *         20
    *     10      30
    *    X  15  25  X
    */
    expect(tree.size).toBe(5);
  });
  test("The max value shouldn't be present in the tree", () => {
    var remainingValues = [];
    tree.inOrderTraversal(v => remainingValues.push(v));
    expect(remainingValues.indexOf(35)).toBe(-1);
  });
  test("Deleting the root should promote a new root", () => {
    tree.deleteMax();
    tree.deleteMax();
    tree.deleteMax();
    /**
    *         10
    *      15    X 
    */
    var remainingValues = [];
    tree.inOrderTraversal(v => remainingValues.push(v));
    expect(tree.root.value).toBe(10);
    expect(tree.size).toBe(2);
  });
  test("Deleting all nodes should make the root equal to null", () => {
    while (tree.size > 0) {
      tree.deleteMin();
    }
    expect(tree.size).toBe(0);
    expect(tree.root).toBeNull();
  });
});
