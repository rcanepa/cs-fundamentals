const utils = require("../utils");

var start, end, garbage;
var unSortedArray = [];
var testSizes = [100, 1000, 10000, 100000];
var testTimeResults = [];

for (let i = 0; i < testSizes[testSizes.length - 1]; i++) {
  unSortedArray[i] = Math.floor(Math.random() * 100000);
}

testSizes.forEach(n => {
  var toBeSorted = unSortedArray.slice(0, n);
  var temp;
  start = +new Date();
  for (var i = 0; i < n; i++) {
    for (var j = 0; j < n; j++) {
      if (toBeSorted[j] > toBeSorted[i]) {
        temp = toBeSorted[i];
        toBeSorted[i] = toBeSorted[j];
        toBeSorted[j] = temp;
      }
    }
  }
  end = +new Date();
  console.log(`n=${n} took ${end - start}ms`);
  testTimeResults.push(end - start);
  // console.log(toBeSorted);
  if (
    JSON.stringify(toBeSorted, null, 2) !==
    JSON.stringify(
      unSortedArray.slice(0, n).sort(utils.compareNumbers),
      null,
      2
    )
  )
    throw new Error(`The array wasn't correctly sorted.`);
});

/*
for (let i = 1; i < testTimeResults.length; i++) {
  console.log(
    `${testTimeResults[i]} / ${testTimeResults[i - 1]} = ${testTimeResults[i] /
      testTimeResults[i - 1] *
      100}%`
  );
}
*/
