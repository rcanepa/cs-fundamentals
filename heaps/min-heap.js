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

var minHeapAPI = {
  peek,
  insert,
  remove,
  size
};

/**
 * Returns the current min element of the heap.
 */
function peek() {
  return this._storage[0];
}

/**
 * Inserts `value` in the last available position of
 * the tree (array) and then it bubbles `value` up until its 
 * parent is smaller than itself.
 * @param {*} value 
 */
function insert(value) {
  var parentPosition, currentPosition;
  this._storage.push(value);
  currentPosition = this._storage.length - 1;
  parentPosition = getParentPosition(currentPosition);
  while (parentPosition !== null) {
    if (this._storage[parentPosition] > value) {
      swap(this._storage, currentPosition, parentPosition);
      currentPosition = parentPosition;
      parentPosition = getParentPosition(parentPosition);
    } else break;
  }
  return this;
}

var h = MinHeap();
console.log(JSON.stringify(h));
h
  .insert(10)
  .insert(100)
  .insert(50)
  .insert(4)
  .insert(40)
  .insert(30)
  .insert(1)
  .insert(-1);
console.log(JSON.stringify(h));

/**
 * Removes the root node of the tree (the smallest value) and then
 * put the last value of the tree in its position. Then this value
 * is pushed down to the bottom until the end of the tree or when
 * it finds a greater value than itself (and stops in that position).
 */
function remove(value) {}

/**
 * Returns the number of elements in the heap.
 */
function size() {
  return this._storage.length;
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

function MinHeap() {
  var newMinHeap = Object.create(minHeapAPI);
  newMinHeap._storage = [];
  return newMinHeap;
}

module.exports = { MinHeap };
