"use strict";
var { createRandomArray, isSorted } = require("./index");

test("createRandomArray - arrays should have the expect length", () => {
  var arr1, arr2, arr3;
  arr1 = createRandomArray(10);
  arr2 = createRandomArray(50);
  arr3 = createRandomArray(100);
  expect(arr1).toHaveLength(10);
  expect(arr2).toHaveLength(50);
  expect(arr3).toHaveLength(100);
});

test("createRandomArray - arrays should be different", () => {
  var arr1, arr2, arr3;
  arr1 = createRandomArray(100);
  arr2 = createRandomArray(100);
  arr3 = createRandomArray(100);
  expect(arr1).not.toBe(arr2);
  expect(arr2).not.toBe(arr3);
  expect(arr1).not.toBe(arr3);
});

test("isSorted - return true on sorted arrays", () => {
  var arr1, arr2;
  arr1 = [1, 2, 3, 4, 100, 5000, 10000];
  arr2 = [];
  expect(isSorted(arr1)).toBeTruthy();
  expect(isSorted(arr2)).toBeTruthy();
});

test("isSorted - should throw on unsorted arrays", () => {
  var arr1;
  arr1 = [900, 1, 340, 200, 10000, 4];
  expect(() => isSorted(arr1)).toThrow();
});
