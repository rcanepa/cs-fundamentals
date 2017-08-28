"use strict";
const utils = require("../utils");

var testSizes = [100, 1000, 10000, 100000];
var testTimeResults = [];

testSizes.forEach(n => {
  var startTime, endTime;
  var toBeSorted, sorted;
  toBeSorted = utils.createRandomArray(n);
  startTime = +new Date();

  sorted = bubbleSort(toBeSorted);

  endTime = +new Date();
  console.log(`n=${n} took ${endTime - startTime}ms`);
  testTimeResults.push(endTime - startTime);

  // Check if the collection is sorted
  utils.isSorted(sorted);
});

function bubbleSort(srcArray) {
  var array, n, temp;
  n = srcArray.length;
  array = srcArray.slice(0, n);
  for (var i = 0; i < n; i++) {
    for (var j = 0; j < n; j++) {
      if (array[j] > array[i]) {
        temp = array[i];
        array[i] = array[j];
        array[j] = temp;
      }
    }
  }
  return array;
}
