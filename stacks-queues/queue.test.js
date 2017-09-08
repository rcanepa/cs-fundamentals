var { Queue } = require("./queue");

var myQueue = new Queue();

test("the size should be zero", () => {
  expect(myQueue.size()).toBe(0);
});

test("adding one element should increase the size to 1", () => {
  myQueue.enqueue("item1");
  expect(myQueue.size()).toBe(1);
});

test("adding one element should return the number of elements of the Queue", () => {
  expect(myQueue.enqueue("item2")).toBe(2);
});

test("adding one more element should increase the size to 3", () => {
  myQueue.enqueue("item3");
  expect(myQueue.size()).toBe(3);
});

test("getting an element should return the one that was first introduced", () => {
  var firstElement = myQueue.dequeue();
  expect(firstElement).toBe("item1");
});

test("getting another one should return the second", () => {
  var secondElement = myQueue.dequeue();
  expect(secondElement).toBe("item2");
  expect(myQueue.size()).toBe(1);
});

test("peek should return the first element on the queue", () => {
  expect(myQueue.peek()).toBe("item3");
  expect(myQueue.size()).toBe(1);
});

test("after peeking, the size of the queue should remain the same", () => {
  expect(myQueue.size()).toBe(1);
});

test("getting the last element should set it size equal to zero", () => {
  myQueue.dequeue();
  expect(myQueue.size()).toBe(0);
});
