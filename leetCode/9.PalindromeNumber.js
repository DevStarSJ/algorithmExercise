/**
 * @param {number} x
 * @return {boolean}
 */
const isPalindrome = (x) => {
  const str = x.toString()
  const reversed = str.split('').reverse().join('')
  return str == reversed
};