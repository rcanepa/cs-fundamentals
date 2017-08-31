"use strict";

/**
 * Node public API.
 * It should be used through Node function creator.
 */
var NodePublicAPI = {
  toString: function toString() {
    return String(this.value);
  }
};

/**
 * Node function creator.
 * It utilices the Node public API through Object.create.
 * @param {*} value 
 */
function Node(value) {
  var newNode = Object.create(NodePublicAPI);
  newNode.value = value;
  newNode.next = null;
  return newNode;
}

/**
 * Linked List public API.
 */
var LinkedListPublicAPI = {
  length: length,
  append: append,
  popHead: popHead,
  peekHead: peekHead,
  peekTail: peekTail,
  forEach: forEach,
  toString: toString
};

/**
 * Returns the length of the ll.
 */
function length() {
  return this.size;
}

/**
 * Append at the end of the LL a new Node
 * with value inside of it.
 * @param {*} value 
 */
function append(value) {
  var newNode = Node(value);
  if (!this.head) {
    this.head = newNode;
    this.tail = newNode;
  } else {
    this.tail.next = newNode;
    this.tail = newNode;
  }
  this.size++;
  return value;
}

/**
 * Removes and returns the first element of the LL.
 */
function popHead() {
  if (!this.head) return undefined;
  if (this.head === this.tail) this.tail = null;
  var poppedValue = this.head.value;
  this.head = this.head.next;
  this.size--;
  return poppedValue;
}

/**
 * Returns the first element of the LL.
 */
function peekHead() {
  if (!this.head) return undefined;
  return this.head.value;
}

/**
 * Returns the last element of the LL.
 */
function peekTail() {
  if (!this.tail) return undefined;
  return this.tail.value;
}

/*
  
*/
/**
 * Execute the callback on every element of the LL.
 * This doesn't allow value mutation. The callback
 * receives a value, not a reference.
 * @param {*} callback 
 */
function forEach(callback) {
  var node = this.head;
  while (node) {
    callback(node.value);
    node = node.next;
  }
}

/**
 * Returns a String representation of the LL.
 */
function toString() {
  var iterator = this.head;
  var values = [];
  while (iterator) {
    values.push(iterator.value);
    iterator = iterator.next;
  }
  return values.join(" -> ");
}

/**
 * Returns a new empty LL.
 */
function LinkedList() {
  var newLinkedList = Object.create(LinkedListPublicAPI);
  newLinkedList.head = null;
  newLinkedList.tail = null;
  newLinkedList.size = 0;
  return newLinkedList;
}

module.exports = { LinkedList: LinkedList };
