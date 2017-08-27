var {
  exponent,
  recursiveExponent,
  recursiveMultiplier,
  recursiveReverse
} = require('./recursionIntro');

// exponent

test('exponent: base 2 exponent 3 should return 8', () => {
  expect(exponent(2, 3)).toBe(8);
})

test('exponent: base 2 exponent 7 should return 128', () => {
  expect(exponent(2, 7)).toBe(128);
})

test('exponent: base 3 exponent 3 should return 27', () => {
  expect(exponent(3, 3)).toBe(27);
})

test('exponent: base 10 exponent 2 should return 100', () => {
  expect(exponent(10, 2)).toBe(100);
})

test('exponent: base 4 exponent 3 should return 64', () => {
  expect(exponent(4, 3)).toBe(64);
})

// recursiveExponent

test('recursiveExponent: base 2 exponent 3 should return 8', () => {
  expect(recursiveExponent(2, 3)).toBe(8);
})

test('recursiveExponent: base 2 exponent 7 should return 128', () => {
  expect(recursiveExponent(2, 7)).toBe(128);
})

test('recursiveExponent: base 3 exponent 3 should return 27', () => {
  expect(recursiveExponent(3, 3)).toBe(27);
})

test('recursiveExponent: base 10 exponent 2 should return 100', () => {
  expect(recursiveExponent(10, 2)).toBe(100);
})

test('recursiveExponent: base 4 exponent 3 should return 64', () => {
  expect(recursiveExponent(4, 3)).toBe(64);
})

// recursiveMultiplier

test('recursiveMultiplier: it should work on empty arrays', () => {
  expect(recursiveMultiplier([], 10)).toEqual([]);
})

test('recursiveMultiplier: [1], 2 => [2]', () => {
  expect(recursiveMultiplier([1], 2)).toEqual([2]);
})

test('recursiveMultiplier: [1, 2, 3], 2 => [2, 4, 6]', () => {
  expect(recursiveMultiplier([1, 2, 3], 2)).toEqual([2, 4, 6]);
})

test('recursiveMultiplier: [10, 15, 30], 10 => [100, 150, 300]', () => {
  expect(recursiveMultiplier([10, 15, 30], 10)).toEqual([100, 150, 300]);
})

test('recursiveMultiplier: it should work with a negative num', () => {
  expect(recursiveMultiplier([10, 15, 30], -10)).toEqual([-100, -150, -300]);
})

// recursiveReverse

test('recursiveReverse: on an empty array should return an empty array', () => {
  expect(recursiveReverse([])).toEqual([]);
})

test('recursiveReverse: on an array with one element should return the same', () => {
  expect(recursiveReverse([1])).toEqual([1]);
})

test('recursiveReverse: it should return the elements in reverse order', () => {
  expect(recursiveReverse([1, 2])).toEqual([2, 1]);
})

test('recursiveReverse: it should return the elements in reverse order', () => {
  expect(recursiveReverse([1, 2, 3, 4, 5])).toEqual([5, 4, 3, 2, 1]);
})
