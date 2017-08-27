var DELIMITER = "|";

var StringQueue = function () {
  this.storage = "";
}

StringQueue.prototype.enqueue = function (element) {
  if (typeof element !== "string") return;
  this.storage += "|" + element;
};

StringQueue.prototype.dequeue = function () {
  if (this.storage.length === 0) return null;
  var endFirstElement = this.storage.substr(1).indexOf(DELIMITER);
  endFirstElement = endFirstElement !== -1 ? endFirstElement : this.storage.length;
  var element = this.storage.substr(1, endFirstElement);
  this.storage = this.storage.slice(endFirstElement + 1);
  return element;
};

StringQueue.prototype.size = function () {
  var elements = this.storage.split(DELIMITER);
  return elements.length - 1;
};

StringQueue.prototype.peek = function () {
  if (this.storage.length === 0) return null;
  var endFirstElement = this.storage.substr(1).indexOf(DELIMITER);
  endFirstElement = endFirstElement !== -1 ? endFirstElement : this.storage.length;
  var element = this.storage.substr(1, endFirstElement);
  return element;
};

var ObjectQueue = function () {
  this.storage = {};
  this.currentId = 0;
}

ObjectQueue.prototype.enqueue = function (element) {
  var elementKey = this.currentId++;
  this.storage[elementKey] = element;
  return Object.keys(this.storage).length;
};

ObjectQueue.prototype.dequeue = function (element) {
  var keys = Object.keys(this.storage);
  var numberOfKeys = keys.length;
  if (numberOfKeys === 0) return null;
  var element = this.storage[keys[0]];
  delete this.storage[keys[0]];
  return element;
};

ObjectQueue.prototype.size = function (element) {
  return Object.keys(this.storage).length;
};

ObjectQueue.prototype.peek = function () {
  var firstKey = Object.keys(this.storage)[0];
  return this.storage[firstKey];
};

exports.StringQueue = StringQueue;
exports.ObjectQueue = ObjectQueue;
