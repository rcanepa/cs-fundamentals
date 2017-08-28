const utils = require("../utils");

var start, end;
var testSizes = [100];
var testTimeResults = [];

testSizes.forEach(n => {
  var toBeSorted, sorted, pivot, minValue, minIndex;
  toBeSorted = utils.createRandomArray(n);
  pivot = 0;
  start = +new Date();

  sorted = insertionSort(toBeSorted);

  end = +new Date();
  console.log(`n=${n} took ${end - start}ms`);
  testTimeResults.push(end - start);

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
