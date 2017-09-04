"use strict";

const ValueNotFoundAPI = {
  parentTree: null,
  setParentTree: function(tree) {
    this.parentTree = tree;
    return this;
  }
};

function ValueNotFound() {
  return Object.create(ValueNotFoundAPI);
}

function isValueNotFound(x) {
  return ValueNotFoundAPI.isPrototypeOf(x);
}

const BTreeAPI = {
  insert: insert,
  contains: contains
};

function insert(value) {
  var result = searchNode(this, value);
  if (isValueNotFound(result)) {
    let parentTree = result.parentTree;
    if (parentTree.value > value) {
      parentTree.left = BTree(value);
    } else {
      parentTree.right = BTree(value);
    }
  } else {
    throw new Error("You cannot repeat values.");
  }
}

function searchNode(tree, value) {
  if (tree.value === value) return tree;
  else if (tree.value > value && tree.left) {
    return searchNode(tree.left, value);
  } else if (tree.value < value && tree.right) {
    return searchNode(tree.right, value);
  } else {
    return ValueNotFound().setParentTree(tree);
  }
}

function contains(value) {
  var result = searchNode(this, value);
  return !isValueNotFound(result);
}

function BTree(value) {
  var newBTree = Object.create(BTreeAPI);
  newBTree.value = value;
  newBTree.left = null;
  newBTree.right = null;
  return newBTree;
}

module.exports = { BTree };
