var { StringQueue } = require("./string-queue");

var myStringQueue = new StringQueue();

test("the size should be zero", () => {
  expect(myStringQueue.size()).toBe(0);
});

test("adding one element should increase the size to 1", () => {
  myStringQueue.enqueue("item1");
  expect(myStringQueue.size()).toBe(1);
});

test("adding two more elements should increase the size to 3", () => {
  myStringQueue.enqueue("item2");
  myStringQueue.enqueue("item3");
  expect(myStringQueue.size()).toBe(3);
});

test("getting an element should return the one that was first introduced", () => {
  var firstElement = myStringQueue.dequeue();
  expect(firstElement).toBe("item1");
});

test("getting another one should return the second", () => {
  var secondElement = myStringQueue.dequeue();
  expect(secondElement).toBe("item2");
  expect(myStringQueue.size()).toBe(1);
});

test("peek should return the first element on the queue", () => {
  expect(myStringQueue.peek()).toBe("item3");
  expect(myStringQueue.size()).toBe(1);
});

test("after peeking, the size of the queue should remain the same", () => {
  expect(myStringQueue.size()).toBe(1);
});

test("getting the last element should set it size equal to zero", () => {
  myStringQueue.dequeue();
  expect(myStringQueue.size()).toBe(0);
});
