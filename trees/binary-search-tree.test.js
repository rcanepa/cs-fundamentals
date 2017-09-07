const { BSTree, validateBSTree } = require("./binary-search-tree");

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

  describe("Deleting arbitrary nodes", () => {
    var tree = BSTree();
    var values = [20, 10, 30, 15, 25, 35];
    values.forEach(v => {
      tree.insert(v);
    });

    test("Deleting a left node shouldn't change the shape of the tree", () => {
      tree.deleteNode(35);
      var rightBranch = tree.root.right;
      // copy branch
      var rightBranchAfterDeletion = Object.assign({}, rightBranch);
      // manually remove right leaf
      rightBranchAfterDeletion.right = null;
      // update the branch size
      rightBranchAfterDeletion.size = 2;
      expect(rightBranch).toEqual(rightBranchAfterDeletion);
    });

    test("When deleting a node with a child, the child should take the place of the parent node", () => {
      /**
       * Tree before deleting
       *        20
       *    10      30
       *      15  25
       */
      tree.deleteNode(10);
      expect(tree.root.left.value).toBe(15);
      expect(tree.root.left.size).toBe(1);
    });

    test("When deleting a node with two children, the smallest child of its right branch should take its place", () => {
      tree.insert(10);
      tree.insert(17);
      tree.insert(16);
      /**
       * Tree before deleting
       *            20
       *     15            30
       * 10      17     25
       *      16
       */
      tree.deleteNode(15);
      /**
       * Tree after deleting 15
       *            20
       *     16            30
       * 10      17     25
       */
      expect(tree.root.left.value).toBe(16);
      expect(tree.root.left.size).toBe(3);
    });
  });
});

describe("Validation", () => {
  test("An invalid tree should throw an error", () => {
    var invalidTree1 = {
      value: 5,
      left: { value: 10, left: null, right: null },
      right: null
    };
    var invalidTree2 = {
      value: 5,
      left: null,
      right: { value: 2, left: null, right: null }
    };
    var invalidTree3 = {
      value: 5,
      left: { value: 10, left: null, right: null },
      right: { value: 2, left: null, right: null }
    };
    expect(() => validateBSTree(invalidTree1)).toThrowError(/Invalid tree/);
    expect(() => validateBSTree(invalidTree2)).toThrowError(/Invalid tree/);
    expect(() => validateBSTree(invalidTree3)).toThrowError(/Invalid tree/);
  });
  test("This tree should valid", () => {
    var validTree1 = {
      value: 5,
      left: { value: 1, left: null, right: null },
      right: null
    };
    var validTree2 = {
      value: 5,
      left: null,
      right: { value: 10, left: null, right: null }
    };
    var validTree3 = {
      value: 5,
      left: { value: 3, left: null, right: null },
      right: { value: 10, left: null, right: null }
    };
    expect(validateBSTree(validTree1)).toBeTruthy();
    expect(validateBSTree(validTree2)).toBeTruthy();
    expect(validateBSTree(validTree3)).toBeTruthy();
  });
});
