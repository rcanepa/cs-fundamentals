const { lsdRadixSort } = require("./lsd-radix-sort");
const { createRandomArray, isSorted } = require("../utils/index");

const W = 7;

/**
 * Transform an integer into a string of a fixed length. If the string number
 * doesn't have `size` digits, random digits are appended to it.
 * @param {int} n : number to be padded.
 * @param {int} size : pad numbers until they have `size` digits.
 */
function leftPad(n, size) {
  n = n + "";
  var numbersToAdd = size - n.length;
  while (numbersToAdd > 0) {
    n += Math.round(Math.random() * 10) % 10 + "";
    numbersToAdd--;
  }
  return n;
}

var testSizes = [100, 1000, 10000, 100000, 1000000];

testSizes.forEach(tSize => {
  const R = 256;
  var sortedData = [];
  var unsortedData = createRandomArray(tSize).map(n => leftPad(n, W));

  var startTime, endTime;
  startTime = +new Date();
  sortedData = lsdRadixSort(unsortedData, W, d => d);
  endTime = +new Date();

  console.log(`n=${tSize} took ${endTime - startTime}ms`);
  isSorted(sortedData);
});
