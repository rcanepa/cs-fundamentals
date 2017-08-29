"use strict";
const utils = require("../utils");

var testSizes = [100, 1000, 10000, 100000, 1000000];
var testTimeResults = [];

testSizes.forEach(n => {
  var toBeSorted, sorted, startTime, endTime;
  toBeSorted = utils.createRandomArray(n);
  startTime = +new Date();

  sorted = mergeSort(toBeSorted);

  endTime = +new Date();
  console.log(`n=${n} took ${endTime - startTime}ms`);
  testTimeResults.push(endTime - startTime);

  // Check if the array is sorted
  utils.isSorted(sorted);
});

function merge(arr1, arr2) {
  var p1, p2, sortedArray;
  p1 = 0;
  p2 = 0;
  sortedArray = [];

  // Copy elements to sortedArray until one of the arrays is completed
  while (p1 < arr1.length && p2 < arr2.length) {
    if (arr1[p1] <= arr2[p2]) {
      sortedArray.push(arr1[p1]);
      p1++;
    } else {
      sortedArray.push(arr2[p2]);
      p2++;
    }
  }

  // Check if one of arrays was not completely copied to sortedArray
  while (p1 < arr1.length) {
    sortedArray.push(arr1[p1]);
    p1++;
  }
  while (p2 < arr2.length) {
    sortedArray.push(arr2[p2]);
    p2++;
  }
  return sortedArray;
}

function mergeSort(srcArray) {
  if (srcArray.length === 1 || srcArray.length === 0) return srcArray;
  var half, leftArray, rightArray;
  half = Math.floor(srcArray.length / 2);
  // split array
  leftArray = mergeSort(srcArray.slice(0, half));
  rightArray = mergeSort(srcArray.slice(half, srcArray.length));
  // merge sorted arrays
  return merge(leftArray, rightArray);
}
