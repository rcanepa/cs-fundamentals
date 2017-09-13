"use strict";
/**
 * In this implementation, the data is kept in an array.
 * The root start at position 0. So for node k (in the array)
 * its children are going to be in positions 2k + 1 and 2k + 2
 * 0  1  2  3  4  5  6  7  8  9
 * k=0, left child=1, right child=2
 * k=1, left child=3, right child=4
 * k=2, left child=5, right child=6
 * and so on...
 */

/**
 * Private functions (not part of the public API).
 */
function getLeftChildPosition(parentPosition) {
  return parentPosition * 2 + 1;
}

function getRightChildPosition(parentPosition) {
  return parentPosition * 2 + 2;
}

function getParentPosition(childPosition) {
  if (childPosition === 0) return null;
  return childPosition % 2 === 1
    ? (childPosition - 1) / 2
    : (childPosition - 2) / 2;
}

function swap(array, position1, position2) {
  if (array.length <= position1 || array.length <= position2)
    throw new Error("Cannot swap elements outside the array.");
  var temp = array[position1];
  array[position1] = array[position2];
  array[position2] = temp;
  return array;
}

/**
 * Public API.
 */
var minHeapAPI = {
  min,
  insert,
  removeMin,
  isEmpty,
  size
};

/**
 * Returns the current min element of the heap.
 */
function min() {
  return this._storage[0];
}

/**
 * Inserts `value` in the last available position of
 * the tree (array) and then it bubbles `value` up until its 
 * parent is smaller than itself.
 * @param {*} value 
 */
function insert(value) {
  var heap = this._storage;
  var parentPosition, currentPosition;
  heap.push(value);
  currentPosition = heap.length - 1;
  parentPosition = getParentPosition(currentPosition);
  while (parentPosition !== null) {
    if (heap[parentPosition] > value) {
      swap(heap, currentPosition, parentPosition);
      currentPosition = parentPosition;
      parentPosition = getParentPosition(parentPosition);
    } else break;
  }
  return this;
}

/**
 * Removes the root node of the tree (the smallest value) and then
 * put the last value of the tree in its position. Then this value
 * is pushed down to the bottom until the end of the tree or when
 * it finds a greater value than itself (and stops in that position).
 */
function removeMin(value) {
  var heap = this._storage;
  if (heap.length === 0) return;

  // Swap the min with the last element
  swap(heap, 0, heap.length - 1);

  // pop the min element
  var min = heap.pop();

  // "bubble down" the value at the root until
  // its final position
  var keepBubbling = true;
  var currentPosition = 0;
  var leftChildPosition = getLeftChildPosition(currentPosition);
  var rightChildPosition = getRightChildPosition(currentPosition);
  while (keepBubbling) {
    // The left child is the smallest of the two
    if (
      heap[leftChildPosition] &&
      (heap[leftChildPosition] < heap[rightChildPosition] &&
        heap[leftChildPosition] < heap[currentPosition])
    ) {
      swap(heap, leftChildPosition, currentPosition);
      currentPosition = leftChildPosition;
      leftChildPosition = getLeftChildPosition(currentPosition);
      rightChildPosition = getRightChildPosition(currentPosition);
    } else if (
      heap[rightChildPosition] &&
      (heap[rightChildPosition] < heap[leftChildPosition] &&
        heap[rightChildPosition] < heap[currentPosition])
    ) {
      // The right child is the smallest of the two
      swap(heap, rightChildPosition, currentPosition);
      currentPosition = rightChildPosition;
      leftChildPosition = getLeftChildPosition(currentPosition);
      rightChildPosition = getRightChildPosition(currentPosition);
    } else {
      // The current element is smaller than its children
      keepBubbling = false;
    }
  }

  return min;
}

/**
 * Returns the number of elements in the heap.
 */
function size() {
  return this._storage.length;
}

/**
 * Returns true if the heap is empty.
 */
function isEmpty() {
  return this._storage.length === 0;
}

function MinHeap() {
  var newMinHeap = Object.create(minHeapAPI);
  newMinHeap._storage = [];
  return newMinHeap;
}

module.exports = { MinHeap };
