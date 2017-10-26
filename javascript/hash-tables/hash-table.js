/**
 * TODO:
 *  - Handle collisions
 */

var hashTableAPI = {
  _count: 0,
  _size: 0,
  _keys: null,
  get: get,
  set: set,
  remove: remove,
  getSize: getSize,
  getElementCount: getElementCount,
  getAllocatedStorage: getAllocatedStorage
};

function getSize() {
  return this._size;
}

function getElementCount() {
  return this._count;
}

function getAllocatedStorage() {
  return this._storage.length;
}

function get(key) {
  return this._storage[hash(key, this.getSize())];
}

function set(key, value) {
  var computedHash = hash(key, this.getSize());
  // The key doesn't exists and the bucket is used (collision detected)
  if (this._keys.indexOf(key) === -1 && this._storage[computedHash]) {
    throw new Error(
      `Collision between key |${key}| and key with value |${this._storage[
        computedHash
      ]}|`
    );
  }
  this._storage[computedHash] = value;
  this._keys.push(key);
  this._count++;
}

function remove(key) {
  var computedHash = hash(key, this.getSize());
  this._storage[computedHash] = undefined;
  this._keys.splice(computedHash, 1);
  this._count--;
}

function hash(key, size) {
  if (typeof key !== "string")
    throw new Error("You can only use a string as key.");
  var hashingCode = 0;
  for (var index = 0; index < key.length; index++) {
    hashingCode = hashingCode + key.charCodeAt(index) * (index + 1);
  }
  return hashingCode % size;
}

function init(hashTable) {
  hashTable._keys = [];
  hashTable._storage = [];
  for (var index = 0; index < hashTable.getSize(); index++) {
    hashTable._storage[index] = undefined;
  }
  return hashTable;
}

function HashTable(initialSize) {
  if (initialSize < 1)
    throw new Error("You can't create a HashTable with size 0 or less.");
  var hashTable = Object.create(hashTableAPI);
  hashTable._size = initialSize || 100;
  init(hashTable);
  return hashTable;
}

module.exports = {
  HashTable
};
