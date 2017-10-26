var DELIMITER = "|";

var StringStack = function(delimiter) {
  this.storage = "";
  this.delimiter = delimiter || DELIMITER;
};

StringStack.prototype.push = function(element) {
  if (typeof element !== "string") return;
  this.storage += this.delimiter + element;
  return this.storage.split(this.delimiter).length - 1;
};

StringStack.prototype.pop = function() {
  var lastBreakPos = this.storage.lastIndexOf(this.delimiter);
  if (lastBreakPos === -1) return null;
  var element = this.storage.slice(lastBreakPos + 1);
  this.storage = this.storage.substr(0, lastBreakPos);
  return element;
};

StringStack.prototype.size = function() {
  var elements = this.storage.split(this.delimiter);
  return elements.length - 1;
};

StringStack.prototype.peek = function(element) {
  var lastBreakPos = this.storage.lastIndexOf(this.delimiter);
  if (lastBreakPos === -1) return null;
  var element = this.storage.slice(lastBreakPos + 1);
  return element;
};

module.exports = {
  StringStack: StringStack
};
