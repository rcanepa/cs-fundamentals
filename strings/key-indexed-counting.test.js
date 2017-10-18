const { keyIndexedCounting } = require("./key-indexed-counting");

describe("It sorts the data", () => {
  let unsortedData = [2, 3, 1, 4, 4, 4, 1, 2];
  const keyFunction = d => d;
  let sortedData = keyIndexedCounting(unsortedData, 5, keyFunction);
  test("sorts the data", () => {
    expect(sortedData).toEqual([1, 1, 2, 2, 3, 4, 4, 4]);
  });
});

describe("It's stable", () => {
  let unsortedData = [
    {
      name: "Thomas",
      age: 30
    },
    {
      name: "Julian",
      age: 23
    },
    {
      name: "Allison",
      age: 27
    },
    {
      name: "Nicholas",
      age: 27
    },
    {
      name: "Ashley",
      age: 27
    },
    {
      name: "Bob",
      age: 41
    },
    {
      name: "Ruslan",
      age: 33
    }
  ];
  const keyFunction = d => d.age;
  let sortedData = keyIndexedCounting(unsortedData, 42, keyFunction);
  test("Preserves the original order (stable)", () => {
    expect(sortedData).toEqual([
      {
        name: "Julian",
        age: 23
      },
      {
        name: "Allison",
        age: 27
      },
      {
        name: "Nicholas",
        age: 27
      },
      {
        name: "Ashley",
        age: 27
      },
      {
        name: "Thomas",
        age: 30
      },
      {
        name: "Ruslan",
        age: 33
      },
      {
        name: "Bob",
        age: 41
      }
    ]);
  });
});
