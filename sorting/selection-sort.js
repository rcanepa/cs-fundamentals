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

function selectionSort(srcArray) {
  var toBeSorted, wall, minValue, minIndex, n;
  n = srcArray.length;
  toBeSorted = srcArray.slice(0, n);
  wall = 0;
  start = +new Date();
  while (wall < n) {
    // O(n)
    var temp;
    minValue = toBeSorted[wall];
    minIndex = wall;
    for (var i = wall; i < n; i++) {
      // O(n)
      if (toBeSorted[i] < minValue) {
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
