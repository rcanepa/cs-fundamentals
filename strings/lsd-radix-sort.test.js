const { lsdRadixSort } = require("./lsd-radix-sort");

describe("It sorts the data", () => {
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
  let sortedData = lsdRadixSort(unsortedData, 3, keyFn);
  test("sorts the data", () => {
    expect(sortedData).toEqual([...unsortedData].sort());
  });
});

describe("It's stable", () => {
  let unsortedData = [
    {
      name: "Thomas",
      age: "30"
    },
    {
      name: "Julian",
      age: "23"
    },
    {
      name: "Allison",
      age: "27"
    },
    {
      name: "Nicholas",
      age: "27"
    },
    {
      name: "Ashley",
      age: "27"
    },
    {
      name: "Bob",
      age: "41"
    },
    {
      name: "Ruslan",
      age: "33"
    }
  ];
  const keyFn = d => d.age;
  let sortedData = lsdRadixSort(unsortedData, 2, keyFn);
  test("Preserves the original order (stable)", () => {
    expect(sortedData).toEqual([
      {
        name: "Julian",
        age: "23"
      },
      {
        name: "Allison",
        age: "27"
      },
      {
        name: "Nicholas",
        age: "27"
      },
      {
        name: "Ashley",
        age: "27"
      },
      {
        name: "Thomas",
        age: "30"
      },
      {
        name: "Ruslan",
        age: "33"
      },
      {
        name: "Bob",
        age: "41"
      }
    ]);
  });
});
