"use strict";
const utils = require("../utils");

var start, end;
var testSizes = [100, 1000, 10000, 100000];
var testTimeResults = [];

testSizes.forEach(n => {
  var toBeSorted, sorted;
  toBeSorted = utils.createRandomArray(n);
  start = +new Date();

  sorted = selectionSort(toBeSorted);

  end = +new Date();
  console.log(`n=${n} took ${end - start}ms`);
  testTimeResults.push(end - start);

  // Check if the collection is sorted
  utils.isSorted(sorted);
});

/**
 * On every iteration, Selection Sort moves the smallest 
 * element to its final position. The `wall` var marks
 * the limit between the sorted and unsorted parts of the
 * array.
 * [0, ..., wall, ..., n - 1]
 *     ^
 * sorted part
 * of the array
 * @param {[*]} srcArray 
 */
function selectionSort(srcArray) {
  var toBeSorted, wall, minValue, minIndex, n;
  n = srcArray.length;
  toBeSorted = srcArray.slice(0, n);
  wall = 0;
  while (wall < n) {
    // O(n)
    var temp;
    minValue = toBeSorted[wall];
    minIndex = wall;
    for (var i = wall; i < n; i++) {
      // O(n) - Loop until finding the smallest element from wall to n
      if (toBeSorted[i] <= minValue) {
        minValue = toBeSorted[i];
        minIndex = i;
      }
    }
    temp = toBeSorted[wall];
    toBeSorted[wall] = toBeSorted[minIndex];
    toBeSorted[minIndex] = temp;
    wall++;
  }
  return toBeSorted;
}
