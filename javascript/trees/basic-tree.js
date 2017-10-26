const treeAPI = {
  addTree: function(value) {
    var newTree = Tree(value);
    this.children.push(newTree);
    return newTree;
  },
  toString: function() {
    return JSON.stringify(this, null, 2);
  }
};

function Tree(value) {
  var newTree = Object.create(treeAPI);
  newTree.value = value;
  newTree.children = [];
  return newTree;
}
/* 
module.exports = { Tree };
var treeRoot = Tree(100);
console.log(treeRoot.toString());
treeRoot.addTree(200).addTree(150);
treeRoot.addTree(50);
console.log(treeRoot.toString());
 */
