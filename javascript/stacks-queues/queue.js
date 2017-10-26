var Queue = function() {
  this.storage = {};
  this.currentId = 0;
};

Queue.prototype.enqueue = function(element) {
  var elementKey = this.currentId++;
  this.storage[elementKey] = element;
  return Object.keys(this.storage).length;
};

Queue.prototype.dequeue = function(element) {
  var keys = Object.keys(this.storage);
  var numberOfKeys = keys.length;
  if (numberOfKeys === 0) return null;
  var element = this.storage[keys[0]];
  delete this.storage[keys[0]];
  return element;
};

Queue.prototype.size = function(element) {
  return Object.keys(this.storage).length;
};

Queue.prototype.peek = function() {
  var firstKey = Object.keys(this.storage)[0];
  return this.storage[firstKey];
};

module.exports = { Queue: Queue };
