//1. Write a function that loops through the numbers n down to 0. If you haven't done so try using a while loop to do this.

var recursiveLoop = function(n) {
  console.log('number ', n);
  if (n <= 0) {
    return n;
  }
 else {
    recursiveLoop(n - 1);
  }
}

// console.log('### recursive loop ###');
// recursiveLoop(5);

//2. Next, try looping just like above except using recursion

var normalLoop = function(n) {
  for(;n>=0;n--) {
    console.log('number ', n);
  }
}

// console.log('### normal loop ###');
// normalLoop(3);

//3. Write a function 'exponent' that takes two arguments base, and expo, uses a while loop to return the exponenet value of the base.

var exponent = function(base, exponent) {
  var result = 1;
  while (exponent >= 1) {
    result *= base;
    exponent--;
  }
  return result;
}

exports.exponent = exponent;

//4. Write a function 'RecursiveExponent' that takes two arguments base, and expo, recursively returns exponent value of the base.

var recursiveExponent = function(base, exponent) {
  if (exponent === 0) return 1;
  else {
    return base * recursiveExponent(base, exponent - 1);
  }
}

exports.recursiveExponent = recursiveExponent;

//5. Write a function 'recursiveMultiplier' that takes two arguments, 'arr and num', and multiplies each arr value into by num and returns an array of the values.

var recursiveMultiplier = function(arr, num) {
  if (arr.length === 0) return arr;
  var lastElement = arr.pop();
  return recursiveMultiplier(arr, num).concat([lastElement * num]);
}

exports.recursiveMultiplier = recursiveMultiplier;

//6. Write a function 'recursiveReverse' that takes an array and uses recursion to return its contents in reverse

var recursiveReverse = function (arr) {
  if (arr.length === 0) return arr;
  var lastElement = arr.pop();
  return [lastElement].concat(recursiveReverse(arr));
}

exports.recursiveReverse = recursiveReverse;
