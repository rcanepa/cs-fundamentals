var start, end, garbage;
var unSortedArray = [];
var testSizes = [100];
var testTimeResults = [];

for (let i = 0; i < testSizes[testSizes.length - 1]; i++) {
  unSortedArray[i] = Math.floor(Math.random() * 100000);
}

testSizes.forEach(n => {
  var toBeSorted = unSortedArray.slice(0, n);
  var temp;
  console.log(`Sorting array of size ${toBeSorted.length}`);
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
  console.log(toBeSorted);
});

for (let i = 1; i < testTimeResults.length; i++) {
  console.log(
    `${testTimeResults[i]} / ${testTimeResults[i - 1]} = ${testTimeResults[i] /
      testTimeResults[i - 1] *
      100}%`
  );
}
