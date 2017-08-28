const utils = require("../utils");

var start, end;
var testSizes = [100, 1000, 10000, 100000];
var testTimeResults = [];

testSizes.forEach(n => {
  var toBeSorted = utils.createRandomArray(n);
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

  // Check if the collection is sorted
  utils.isSorted(toBeSorted);
});
