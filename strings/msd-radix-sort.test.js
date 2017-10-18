const { MSDRadixSort } = require("./msd-radix-sort");

describe("It works with fixed length strings", () => {
  let unsortedData = [
    "4PGC938",
    "2IYE230",
    "3CI0720",
    "1ICK750",
    "1OHV845",
    "4JZY524",
    "1ICK750",
    "3CI0720",
    "1OHV845",
    "1OHV845",
    "2RLA629",
    "2RLA629",
    "3ATW723"
  ];
  const keyFn = d => d;
  let sortedData = MSDRadixSort(unsortedData);
  test("sorts the data", () => {
    expect(sortedData).toEqual(unsortedData.sort());
  });
});

describe("It works with variable length strings", () => {
  let unsortedData = [
    "A4PGC938",
    "2IYE23",
    "3CI20",
    "1ICK750",
    "A15",
    "4JZY24",
    "1ICK750",
    "3CI0720",
    "OHV845",
    "B1OHV845",
    "2RLA629",
    "RLA629",
    "3ATW723"
  ];
  const keyFn = d => d;
  let sortedData = MSDRadixSort(unsortedData);
  console.log(sortedData);
  test("sorts the data", () => {
    expect(sortedData).toEqual(unsortedData.sort());
  });
});
