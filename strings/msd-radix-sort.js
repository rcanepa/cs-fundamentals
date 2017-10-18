/** MSD (most significant digit) string sort algorithm.
This sorting algorithm works sorting strings character by character
from left to right.

Characteristics:
    - Stable (preserves original order).

Main differences with the LSD string sort algorithm:
    - Runs from left to right.
    - It's recursive.
*/

"use strict";

// Radix: number of different possible characters.
// 256 -> Extended ASCII.
const R = 256;

function initializeArray(size, defaultValue) {
  var a = [];
  for (var i = 0; i < size; i++) a.push(defaultValue);
  return a;
}

function charCode(str, digit) {
  if (digit < str.length) {
    return str.charCodeAt(digit);
  } else {
    return -1;
  }
}

function MSDRadixSort(data) {
  var sortedData = [...data];
  var aux = initializeArray(data.length, undefined);
  msdRadixSort(sortedData, aux, 0, data.length - 1, 0);
  return sortedData;
}

function msdRadixSort(data, aux, low, high, digit) {
  if (high <= low) return;

  // R + 2 because we need one more space to accomodate the -1 case.
  var count = initializeArray(R + 2, 0);

  // Phase 1: compute frequencies.
  for (var i = low; i <= high; i++) {
    count[charCode(data[i], digit) + 2]++;
  }

  // Phase 2: compute indices (starting points for each letter/character).
  for (var r = 0; r <= R; r++) {
    count[r + 1] += count[r];
  }

  // Phase 3: distribute data.
  for (var i = low; i <= high; i++) {
    var newPosition = count[charCode(data[i], digit) + 1]++;
    aux[newPosition] = data[i];
  }

  // Phase 4: copy sorted data into data.
  for (var i = low; i <= high; i++) {
    data[i] = aux[i - low];
  }

  // Sort every partition
  for (var r = 0; r < R; r++) {
    msdRadixSort(data, aux, low + count[r], low + count[r + 1] - 1, digit + 1);
  }
}

module.exports = {
  MSDRadixSort
};
