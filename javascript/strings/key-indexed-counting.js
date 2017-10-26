/* Key-indexed Counting sorting algorithm.
Extremely effective sorting algorithm for data in which the sorting keys
are small integers.

The algorithm works in three phase:
  1. Count the frequency of each integer/character.
  2. Find the starting point (indices) on the sorted array for every integer/character.
  3. Distribute de data according to the result of phase 2.

Characteristics:
    - Stable (preserves original order).
    - Linear time O(n) when R is within a constant factor o N and when keys
      are integers between 0 and R - 1.

Applications:
    - Sort by area code.
    - Sort by string first letter.
    - Sort by age.*/

function initializeArray(size, defaultValue) {
  var a = [];
  for (var i = 0; i < size; i++) a.push(defaultValue);
  return a;
}

function keyIndexedCounting(data, r, keyFn) {
  var count = initializeArray(r + 1, 0);
  sortedData = initializeArray(data.length, undefined);

  // Phase 1
  for (var i = 0; i < data.length; i++) {
    count[keyFn(data[i]) + 1]++;
  }

  // Phase 2
  for (var i = 0; i < r; i++) {
    count[i + 1] += count[i];
  }

  // Phase 3
  for (var i = 0; i < data.length; i++) {
    finalPosition = count[keyFn(data[i])];
    count[keyFn(data[i])]++;
    sortedData[finalPosition] = data[i];
  }

  return sortedData;
}

module.exports = {
  keyIndexedCounting
};
