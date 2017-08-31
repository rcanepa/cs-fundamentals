"use strict";

var { LinkedList } = require("./linked-list");

var ll;
beforeEach(() => {
  ll = LinkedList();
  ll.append(10);
  ll.append(20);
});

test("it should append at the start of the linked list", () => {
  expect(ll.head.value).toBe(10);
  expect(ll.head.next.value).toBe(20);
  expect(ll.head.next.next).toBe(null);
});

test("peekHead", () => {
  expect(ll.peekHead()).toBe(10);
});

test("peekTail", () => {
  expect(ll.peekTail()).toBe(20);
});

test("popHead", () => {
  expect(ll.popHead()).toBe(10);
  expect(ll.peekHead()).toBe(20);
});

test("forEach", () => {
  var values = [];
  ll.forEach(v => {
    values.push(v);
  });
  expect(values).toHaveLength(2);
  expect(values).toEqual([10, 20]);
});

test("length", () => {
  expect(ll.length()).toBe(2);
});
