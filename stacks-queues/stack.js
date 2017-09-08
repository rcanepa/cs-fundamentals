var Stack = function() {
  this.storage = {};
  this.currentId = 0;
};

Stack.prototype.push = function(element) {
  var elementKey = this.currentId++;
  this.storage[elementKey] = element;
  return this.currentId;
};

Stack.prototype.pop = function(element) {
  if (this.currentId === 0) return null;
  var idToPop = --this.currentId;
  var element = this.storage[idToPop];
  delete this.storage[idToPop];
  return element;
};

Stack.prototype.size = function(element) {
  return Object.keys(this.storage).length;
};

Stack.prototype.peek = function(element) {
  if (this.currentId === 0) return null;
  var element = this.storage[this.currentId - 1];
  return element;
};

module.exports = { Stack: Stack };
