"use strict";
const utils = require("../utils");

var testSizes = [100];
var testTimeResults = [];

testSizes.forEach(n => {
  var toBeSorted, sorted;
  var startTime, endTime;
  toBeSorted = utils.createRandomArray(n);
  startTime = +new Date();

  sorted = insertionSort(toBeSorted);

  endTime = +new Date();
  console.log(`n=${n} took ${endTime - startTime}ms`);
  testTimeResults.push(endTime - startTime);

  // Check if the array is sorted
  utils.isSorted(sorted);
});

function insertionSort(srcArray) {
  var temp, array;
  array = srcArray.slice(0, srcArray.length);
  for (var i = 1; i < array.length; i++) {
    // O(n)
    for (var j = i; j >= 0; j--) {
      // O(n)
      if (array[j] < array[j - 1]) {
        temp = array[j];
        array[j] = array[j - 1];
        array[j - 1] = temp;
      }
    }
  }
  return array;
}
