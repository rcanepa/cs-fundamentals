const { BTree } = require("./binary-search-tree");

var values = [200, 50, 70, 76, 26, 65, 150];
var tree = BTree(100);

values.forEach(v => {
  tree.insert(v);
});

console.log(JSON.stringify(tree, null, 2));

console.log(values.length === values.filter(v => tree.contains(v)).length);
