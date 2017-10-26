var { HashTable } = require("./hash-table");

test("It should throw when creating with size 0 or less", () => {
  expect(() => HashTable(0)).toThrow();
  expect(() => HashTable(-1)).toThrow();
});

test("When no size is passed, the default size is 100", () => {
  var ht = HashTable();
  expect(ht.getSize()).toBe(100);
  expect(ht.getAllocatedStorage()).toBe(100);
});

describe("Adding, getting and removing keys", () => {
  var ht = HashTable(1000);
  ht.set("renzo", 31);
  ht.set("canepa", 3);
  ht.set("dagny", 1);
  ht.set("james", 91);
  ht.set("alice", 38);
  test("Setting and getting keys", () => {
    expect(ht.get("renzo")).toBe(31);
    expect(ht.get("canepa")).toBe(3);
    expect(ht.get("dagny")).toBe(1);
    expect(ht.get("james")).toBe(91);
    expect(ht.get("alice")).toBe(38);
    expect(ht.getElementCount()).toBe(5);
  });

  test("Values of deleted keys shouldn't be available", () => {
    ht.remove("renzo");
    ht.remove("alice");
    expect(ht.get("renzo")).toBeUndefined();
    expect(ht.get("alice")).toBeUndefined();
    expect(ht.get("canepa")).toBe(3);
    expect(ht.get("dagny")).toBe(1);
    expect(ht.get("james")).toBe(91);
    expect(ht.getElementCount()).toBe(3);
  });
});
