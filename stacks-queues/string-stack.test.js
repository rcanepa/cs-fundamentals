var { StringStack } = require("./string-stack");

var myStringStack = new StringStack();

test("the size should be zero", () => {
  expect(myStringStack.size()).toBe(0);
});

test("adding one element should increase the size to 1", () => {
  myStringStack.push("item1");
  expect(myStringStack.size()).toBe(1);
});

test("adding one element should return the number of elements in the stack", () => {
  expect(myStringStack.push("item2")).toBe(2);
});

test("adding one more element should increase the size to 3", () => {
  myStringStack.push("item3");
  expect(myStringStack.size()).toBe(3);
});

test("getting an element should return the last one added", () => {
  var lastElement = myStringStack.pop();
  expect(lastElement).toBe("item3");
});

test("getting another one should return the second", () => {
  var secondElement = myStringStack.pop();
  expect(secondElement).toBe("item2");
  expect(myStringStack.size()).toBe(1);
});

test("peek should return the top element on the stack", () => {
  expect(myStringStack.peek()).toBe("item1");
  expect(myStringStack.size()).toBe(1);
});

test("after peeking, the size of the queue should remain the same", () => {
  expect(myStringStack.size()).toBe(1);
});

test("getting the last element should set it size equal to zero", () => {
  myStringStack.pop();
  expect(myStringStack.size()).toBe(0);
});
