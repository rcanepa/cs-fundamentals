"use strict";
module.exports = {
  compareNumbers: compareNumbers,
  isSorted: isSorted,
  createRandomArray: createRandomArray
};

function compareNumbers(a, b) {
  return a - b;
}

function isSorted(collection, compareFunction) {
  if (compareFunction === undefined) {
    compareFunction = (a, b) => a <= b;
  }
  for (var i = 1; i < collection.length; i++) {
    if (!compareFunction(collection[i - 1], collection[i])) {
      throw new Error(
        `The collection is not sorted. Index: ${i - 1} = ${collection[
          i - 1
        ]}, Index: ${i} = ${collection[i]}`
      );
    }
  }
  return true;
}

function createRandomArray(arraySize, seed = 1) {
  var x;
  var array = [];
  for (var i = 0; i < arraySize; i++) {
    x = Math.sin(seed++) * 10000;
    x = x - Math.floor(x);
    array[i] = Math.floor(x * 100000);
  }
  return array;
}
