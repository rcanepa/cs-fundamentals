var DELIMITER = "|";

var StringQueue = function(delimiter) {
  this.storage = "";
  this.delimiter = delimiter || DELIMITER;
};

StringQueue.prototype.enqueue = function(element) {
  if (typeof element !== "string") return;
  this.storage += "|" + element;
};

StringQueue.prototype.dequeue = function() {
  if (this.storage.length === 0) return null;
  var endFirstElement = this.storage.substr(1).indexOf(this.delimiter);
  endFirstElement =
    endFirstElement !== -1 ? endFirstElement : this.storage.length;
  var element = this.storage.substr(1, endFirstElement);
  this.storage = this.storage.slice(endFirstElement + 1);
  return element;
};

StringQueue.prototype.size = function() {
  var elements = this.storage.split(this.delimiter);
  return elements.length - 1;
};

StringQueue.prototype.peek = function() {
  if (this.storage.length === 0) return null;
  var endFirstElement = this.storage.substr(1).indexOf(this.delimiter);
  endFirstElement =
    endFirstElement !== -1 ? endFirstElement : this.storage.length;
  var element = this.storage.substr(1, endFirstElement);
  return element;
};

module.exports = {
  StringQueue: StringQueue
};
