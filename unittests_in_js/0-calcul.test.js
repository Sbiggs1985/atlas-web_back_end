const assert = require('assert');
const calculateNumber = require('./0-calcul');

describe('calculateNumber', () => {
  const testCases = [
    { a: 1.0, b: 2.0, expected: 3, description: 'floating point whole numbers' },
    { a: 1.0, b: 2.4, expected: 3, description: 'rounding down b\'s floating point fractional number' },
    { a: 1.4, b: 2.4, expected: 3, description: 'rounding down a and b\'s floating point fractional number' },
    { a: 1.4, b: 2.0, expected: 3, description: 'rounding down a\'s floating point fractional number' },
    { a: 1.0, b: 2.5, expected: 4, description: 'rounding up b\'s floating point fractional numbers' },
    { a: 2.6, b: 2.5, expected: 6, description: 'rounding up a and b\'s floating point fractional numbers' },
    { a: 2.6, b: 2.0, expected: 5, description: 'rounding up a\'s floating point fractional numbers' },
    { a: 2.499999, b: 3.499999, expected: 5, description: 'rounding down a and b floating point fractional numbers with trailing 9\'s' },
  ];

  testCases.forEach(({ a, b, expected, description }) => {
    it(description, () => {
      assert.strictEqual(calculateNumber(a, b), expected);
    });
  });
});