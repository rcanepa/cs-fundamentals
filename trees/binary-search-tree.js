"use strict";

function computeNodeSize(node) {
  return (
    1 +
    ((node.right && node.right.size) || 0) +
    ((node.left && node.left.size) || 0)
  );
}

function BSTreeNode(value) {
  return {
    value: value,
    left: null,
    right: null,
    size: 1
  };
}

const ValueNotFoundAPI = {
  parentNode: null,
  setParentNode: function(node) {
    this.parentNode = node;
    return this;
  }
};

function ValueNotFound() {
  return Object.create(ValueNotFoundAPI);
}

function isValueNotFound(x) {
  return ValueNotFoundAPI.isPrototypeOf(x);
}

const BSTreeAPI = {
  size: 0,
  root: null,
  insert: insert,
  contains: contains,
  deleteMax: deleteMax,
  deleteMin: deleteMin,
  deleteNode: deleteNode,
  preOrderTraversal: preOrderTraversal,
  inOrderTraversal: inOrderTraversal,
  postOrderTraversal: postOrderTraversal
};

function validateBSTree(node) {
  if (
    (node.left && node.left.value > node.value) ||
    (node.right && node.right.value < node.value)
  ) {
    throw new Error(
      `Invalid tree. root=${node.value}, left=${node.left
        ? node.left.value
        : 0}, right=${node.right ? node.right.value : 0}`
    );
  }
  if (node.left) validateBSTree(node.left);
  if (node.right) validateBSTree(node.right);
  return true;
}

function _insert(node, value) {
  if (node.value === value) {
    throw new Error("The element was already present in the tree.");
  } else if (node.value > value && node.left) {
    node.left = _insert(node.left, value);
  } else if (node.value < value && node.right) {
    node.right = _insert(node.right, value);
  } else if (node.value > value && !node.left) {
    node.left = BSTreeNode(value);
  } else if (node.value < value && !node.right) {
    node.right = BSTreeNode(value);
  }
  node.size = computeNodeSize(node);
  return node;
}

function insert(value) {
  if (!this.root) {
    this.root = BSTreeNode(value);
  } else {
    this.root = _insert(this.root, value);
  }
  this.size = this.root.size;
  return this.root;
}

function searchNode(node, value) {
  if (node.value === value) return node;
  if (node.value > value && node.left) {
    return searchNode(node.left, value);
  }
  if (node.value < value && node.right) {
    return searchNode(node.right, value);
  }
  return ValueNotFound().setParentNode(node);
}

function contains(value) {
  var result = searchNode(this, value);
  return !isValueNotFound(result);
}

function _deleteMax(node) {
  if (node.right) {
    node.right = _deleteMax(node.right);
    node.size = computeNodeSize(node);
    return node;
  }
  return node.left ? node.left : null;
}

function deleteMax() {
  if (this.root) {
    this.root = _deleteMax(this.root);
    this.size--;
  }
}

function _deleteMin(node) {
  if (node.left) {
    node.left = _deleteMin(node.left);
    node.size = computeNodeSize(node);
    return node;
  }
  return node.right ? node.right : null;
}

function deleteMin() {
  if (this.root) {
    this.root = _deleteMin(this.root);
    this.size--;
  }
}

function _deleteNode(node, value) {
  if (node.value === value) {
    // case 1: the node is a leaf
    if (!node.left && !node.right) {
      return null;
      // case 2: the node has one child
    } else if (!node.left && node.right) {
      return node.right;
      // case 3: the node has one child
    } else if (node.left && !node.right) {
      return node.left;
      // case 4: the node has two children
      // replace node with the smallest child of its right branch
    } else {
      var smallestNode = node.right;
      var smallestNodeParent = null;
      // find the smallest one of its right branch
      while (smallestNode.left) {
        smallestNodeParent = smallestNode;
        smallestNode = smallestNode.left;
      }
      // remove it from its parent
      smallestNodeParent.left = null;
      smallestNodeParent.size = computeNodeSize(smallestNodeParent);
      // make the smallest take the place of the one being deleted
      smallestNode.left = node.left;
      smallestNode.right = node.right;
      smallestNode.size = computeNodeSize(smallestNode);
      // return it
      return smallestNode;
    }
  } else if (node.value > value && node.left) {
    node.left = _deleteNode(node.left, value);
  } else if (node.value < value && node.right) {
    node.right = _deleteNode(node.right, value);
  }
  node.size = computeNodeSize(node);
  return node;
}

function deleteNode(value) {
  if (this.root) {
    this.root = _deleteNode(this.root, value);
  }
}

function _preOrderTraversal(node, cb) {
  if (!node) return;
  cb(node.value);
  _preOrderTraversal(node.left, cb);
  _preOrderTraversal(node.right, cb);
}

function preOrderTraversal(cb) {
  _preOrderTraversal(this.root, cb);
}

function _inOrderTraversal(node, cb) {
  if (!node) return;
  _inOrderTraversal(node.left, cb);
  cb(node.value);
  _inOrderTraversal(node.right, cb);
}

function inOrderTraversal(cb) {
  _inOrderTraversal(this.root, cb);
}

function _postOrderTraversal(node, cb) {
  if (!node) return;
  _postOrderTraversal(node.left, cb);
  _postOrderTraversal(node.right, cb);
  cb(node.value);
}

function postOrderTraversal(cb) {
  _postOrderTraversal(this.root, cb);
}

function BSTree(value) {
  var newBTree = Object.create(BSTreeAPI);
  if (value) {
    newBTree.root = BSTreeNode(value);
    newBTree.size = 1;
  }
  return newBTree;
}

module.exports = { BSTree, validateBSTree };
