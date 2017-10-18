/*LSD (least significant digit) string sort algorithm.
This algorithm is based on the Key-indexed counting sorting algorithm. The
main difference is that LSD run the same operation for W characters instead
of just 1 integer. It is assumed that strings are fixed length and that W
is the length of them.

Characteristics:
    - Stable (preserves original order).
    - Linear time: O(N * W).

E.g.:

Given the strings:
    [
        "4PGC938",
        "2IYE230",
        "3CI0720"
    ]

The algorithm is going to sort them through 7 iterations (W = 7). The process
is going to sort them char by char starting from right to left (from the least
significant 'digit').

After the first iteration, the result is going to be:
    [
        "2IYE230",
        "3CI0720"
        "4PGC938",
    ]

After the second:
    [
        "3CI0720"
        "2IYE230",
        "4PGC938",
    ]

And so on until the end:
    [
        "2IYE230",
        "3CI0720"
        "4PGC938",
    ]
*/

function initializeArray(size, defaultValue) {
  var a = [];
  for (var i = 0; i < size; i++) a.push(defaultValue);
  return a;
}

/**
 * LSD radix sort algorithm.
 * @param {*} data  : array of data to be sorted.
 * @param {*} W     : fixed length of the string key.
 * @param {*} keyFn : function that operates on a data element an return its key.
 */
function lsdRadixSort(data, W = 0, keyFn) {
  // r = radix. Number of possible characters.
  // r = 256 -> extended ASCII.

  const R = 256;
  const rowsToSort = data.length;

  if (W === 0) W = data[0].length;

  var partiallySortedData = initializeArray(data.length, undefined);

  // Run Key-indexed Counting for every char from rigth to left.
  for (var i = W - 1; i >= 0; i--) {
    var count = initializeArray(R + 1, 0);

    // Phase 1: compute frequencies.
    for (var j = 0; j < rowsToSort; j++) {
      var asciiCode = keyFn(data[j]).charCodeAt(i);
      count[asciiCode + 1]++;
    }

    // Phase 2: compute indices (starting points).
    for (var r = 0; r < R; r++) {
      count[r + 1] += count[r];
    }

    // Phase 3: distribute data.
    for (var k = 0; k < rowsToSort; k++) {
      dataPosition = count[keyFn(data[k]).charCodeAt(i)];
      count[keyFn(data[k]).charCodeAt(i)]++;
      partiallySortedData[dataPosition] = data[k];
    }

    // Copy the result to the original array.
    for (var l = 0; l < rowsToSort; l++) {
      data[l] = partiallySortedData[l];
    }
  }

  return data;
}

module.exports = {
  lsdRadixSort
};
