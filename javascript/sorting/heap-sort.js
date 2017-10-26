/**
 * Heapsort implementation using heaps from 
 * the heaps folder.
 */

"use strict";
const { MinHeap } = require("../heaps/min-heap");
const { MaxHeap } = require("../heaps/max-heap");
const utils = require("../utils");

var testSizes = [100, 1000, 10000, 100000, 1000000];
var testTimeResults = [];

testSizes.forEach(n => {
  var toBeSorted, sorted, startTime, endTime;
  toBeSorted = utils.createRandomArray(n, 1);
  startTime = +new Date();

  sorted = heapSort(toBeSorted);

  endTime = +new Date();
  console.log(`n=${n} took ${endTime - startTime}ms`);
  testTimeResults.push(endTime - startTime);

  // Check if the array is sorted
  utils.isSorted(sorted);
});

function heapSort(array) {
  var h = MinHeap(array);
  var sortedArray = [];
  while (h.size() > 0) {
    sortedArray.push(h.removeMin());
  }
  return sortedArray;
}

module.exports = {
  heapSort
};
