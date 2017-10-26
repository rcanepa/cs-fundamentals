"use strict";
/**
 * In this implementation, the data is kept in an array.
 * The root start at position 0. Children of some node k
 * are found in positions 2k + 1 and 2k + 2.
 * 0  1  2  3  4  5  6  7  8  9
 * k=0, left child=1, right child=2
 * k=1, left child=3, right child=4
 * k=2, left child=5, right child=6
 * and so on...
 */

/**
 * Private functions (not part of the public API).
 */

function validateHeap(heap, currentPosition = 0) {
  var leftChildPosition = getLeftChildPosition(currentPosition);
  var rightChildPosition = getRightChildPosition(currentPosition);
  if (!heap._storage[leftChildPosition] || !heap._storage[rightChildPosition]) {
    return true;
  }
  if (
    heap._storage[leftChildPosition] > heap._storage[currentPosition] ||
    heap._storage[rightChildPosition] > heap._storage[currentPosition]
  ) {
    throw new Error(
      `Invalid heap. Parent = ${heap._storage[
        currentPosition
      ]}, leftChild = ${heap._storage[leftChildPosition]}, rightChild = ${heap
        ._storage[rightChildPosition]}.`
    );
  } else {
    return validateHeap(heap, leftChildPosition);
    return validateHeap(heap, rightChildPosition);
  }
}

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

function isLess(array, position1, position2) {
  return array[position1] < array[position2];
}

/**
 * Public API.
 */
var maxHeapAPI = {
  max,
  insert,
  removeMax,
  isEmpty,
  size,
  merge
};

/**
 * Returns the current max element of the heap.
 */
function max() {
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
    if (heap[parentPosition] < value) {
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
function removeMax(value) {
  var heap = this._storage;
  if (heap.length === 0) return;

  // Swap the max with the last element
  swap(heap, 0, heap.length - 1);

  // pop the max element
  var max = heap.pop();

  // "bubble down" the value at the root until
  // its final position
  var currentPosition = 0;
  var leftChildPosition = getLeftChildPosition(currentPosition);
  var rightChildPosition = getRightChildPosition(currentPosition);
  while (leftChildPosition < this.size() && rightChildPosition < this.size()) {
    if (
      isLess(heap, leftChildPosition, currentPosition) &&
      isLess(heap, rightChildPosition, currentPosition)
    ) {
      break;
    } else {
      if (isLess(heap, rightChildPosition, leftChildPosition)) {
        swap(heap, leftChildPosition, currentPosition);
        currentPosition = leftChildPosition;
        leftChildPosition = getLeftChildPosition(currentPosition);
        rightChildPosition = getRightChildPosition(currentPosition);
      } else {
        swap(heap, rightChildPosition, currentPosition);
        currentPosition = rightChildPosition;
        leftChildPosition = getLeftChildPosition(currentPosition);
        rightChildPosition = getRightChildPosition(currentPosition);
      }
    }
  }

  if (
    heap[leftChildPosition] &&
    isLess(heap, currentPosition, leftChildPosition)
  ) {
    swap(heap, currentPosition, leftChildPosition);
  }

  if (
    heap[rightChildPosition] &&
    isLess(heap, currentPosition, rightChildPosition)
  ) {
    swap(heap, currentPosition, rightChildPosition);
  }

  return max;
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

/**
 * Creates a new Heap by merging two of them.
 * @param {MaxHeap} theOtherHeap 
 */
function merge(theOtherHeap) {
  var allElements = this._storage.concat(theOtherHeap._storage);
  return MaxHeap(allElements);
}

function MaxHeap(initialData) {
  initialData = initialData || [];
  if (Object.prototype.toString.call(initialData) !== "[object Array]")
    throw new Error("You can only initialize the Heap with an array.");
  var newMaxHeap = Object.create(maxHeapAPI);
  newMaxHeap._storage = [];
  initialData.forEach(function(element) {
    newMaxHeap.insert(element);
  }, this);
  return newMaxHeap;
}

module.exports = { MaxHeap };
