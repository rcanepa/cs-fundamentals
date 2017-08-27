const fs = require("fs");
const utils = require("../utils");

var start, end, garbage;
var unSortedArray = [];
var testSizes = [100, 1000, 10000, 100000];
var testTimeResults = [];

for (let i = 0; i < testSizes[testSizes.length - 1]; i++) {
  unSortedArray[i] = Math.floor(Math.random() * 100000);
}

testSizes.forEach(n => {
  var toBeSorted, pivot, minValue, minIndex;
  toBeSorted = unSortedArray.slice(0, n);
  pivot = 0;
  start = +new Date();
  while (pivot < n) {
    var temp;
    minValue = toBeSorted[pivot];
    minIndex = pivot;
    for (var i = pivot; i < n; i++) {
      if (toBeSorted[i] < minValue) {
        minValue = toBeSorted[i];
        minIndex = i;
      }
    }
    temp = toBeSorted[pivot];
    toBeSorted[pivot] = toBeSorted[minIndex];
    toBeSorted[minIndex] = temp;
    pivot++;
  }
  end = +new Date();
  console.log(`n=${n} took ${end - start}ms`);
  testTimeResults.push(end - start);

  if (
    JSON.stringify(toBeSorted, null, 2) !==
    JSON.stringify(
      unSortedArray.slice(0, n).sort(utils.compareNumbers),
      null,
      2
    )
  )
    throw new Error(`The array wasn't correctly sorted.`);
  /*
  // Validate sorting result
  var filename = `selection_sort_${n}.out`;
  fs.writeFile(filename, toBeSorted.join("\n"), err => {
    if (err) console.log(`Error writing file ${filename}: ${err}`);
  });
  fs.writeFile(
    `${filename}.comp`,
    unSortedArray.slice(0, n).sort(utils.compareNumbers).join("\n"),
    () => {}
  );
  */
});
