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
  preOrderTraversal: preOrderTraversal,
  inOrderTraversal: inOrderTraversal,
  postOrderTraversal: postOrderTraversal
};

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
    node.size = node.right && node.right.size + node.left && node.left.size;
    return node;
  }
  return node.left ? node.left : null;
}

function deleteMax() {
  if (this.size > 0) {
    this.root = _deleteMax(this.root);
    this.size--;
  }
}

function _deleteMin(node) {
  if (node.left) {
    node.left = _deleteMin(node.left);
    node.size =
      1 +
      ((node.right && node.right.size) || 0) +
      ((node.left && node.left.size) || 0);
    return node;
  }
  return node.right ? node.right : null;
}

function deleteMin() {
  if (this.size > 0) {
    this.root = _deleteMin(this.root);
    this.size--;
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

module.exports = { BSTree };
