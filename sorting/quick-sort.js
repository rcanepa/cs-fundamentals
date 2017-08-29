"use strict";
const utils = require("../utils");

var testSizes = [100, 1000, 10000, 100000, 1000000];
var testTimeResults = [];

testSizes.forEach(n => {
  var toBeSorted, sorted, startTime, endTime;
  toBeSorted = utils.createRandomArray(n);
  startTime = +new Date();

  sorted = quickSort(toBeSorted);

  endTime = +new Date();
  console.log(`n=${n} took ${endTime - startTime}ms`);
  testTimeResults.push(endTime - startTime);

  // Check if the array is sorted
  utils.isSorted(sorted);
});

function swap(array, i, j) {
  var temp = array[i];
  array[i] = array[j];
  array[j] = temp;
}

function partition(array, low, high) {
  // array[low] is the pivot
  var lIndex = low;
  var rIndex = high + 1;
  while (true) {
    // From the left, search an element equal or bigger than the pivot
    while (array[++lIndex] <= array[low]) if (lIndex === high) break;
    // From the right, search an element smaller than the pivot
    while (array[--rIndex] > array[low]) if (rIndex === low) break;
    // This signal the end of the search
    if (lIndex >= rIndex) break;
    swap(array, lIndex, rIndex);
  }
  // Swap the pivot to its final position
  swap(array, rIndex, low);
  return rIndex;
}

function sort(array, low, high) {
  if (low >= high) return array;
  var partitionPivot = partition(array, low, high);
  sort(array, low, partitionPivot - 1);
  sort(array, partitionPivot + 1, high);
}

// Wrapper to avoid giving the user the responsability
// of computing the array boundaries
function quickSort(array) {
  sort(array, 0, array.length - 1);
  return array;
}
