var DELIMITER = "|";

var StringStack = function () {
  this.storage = "";
}

StringStack.prototype.push = function (element) {
  if (typeof element !== "string") return;
  this.storage += DELIMITER + element;
  return this.storage.split(DELIMITER).length - 1;
};

StringStack.prototype.pop = function () {
  var lastBreakPos = this.storage.lastIndexOf(DELIMITER);
  if (lastBreakPos === -1) return null;
  var element = this.storage.slice(lastBreakPos + 1);
  this.storage = this.storage.substr(0, lastBreakPos);
  return element;
};

StringStack.prototype.size = function () {
  var elements = this.storage.split(DELIMITER);
  return elements.length - 1;
};

StringStack.prototype.peek = function (element) {
  var lastBreakPos = this.storage.lastIndexOf(DELIMITER);
  if (lastBreakPos === -1) return null;
  var element = this.storage.slice(lastBreakPos + 1);
  return element;
};

var ObjectStack = function () {
  this.storage = {};
  this.currentId = 0;
}

ObjectStack.prototype.push = function (element) {
  var elementKey = this.currentId++;
  this.storage[elementKey] = element;
  return this.currentId;
};

ObjectStack.prototype.pop = function (element) {
  if (this.currentId === 0) return null;
  var idToPop = --this.currentId;
  var element = this.storage[idToPop];
  delete this.storage[idToPop];
  return element;
};

ObjectStack.prototype.size = function (element) {
  return Object.keys(this.storage).length;
};

ObjectStack.prototype.peek = function (element) {
  if (this.currentId === 0) return null;
  var element = this.storage[this.currentId - 1];
  return element;
};

exports.StringStack = StringStack;
exports.ObjectStack = ObjectStack;
