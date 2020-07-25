/**
 * @param {string} str
 * @return {number}
 */

const INT_MAX = Math.pow(2, 31) - 1
const INT_MIN = -(INT_MAX + 1)
const ALLOWED_STR = '1234567890-+'.split('')

const myAtoi = (str) => {
  let passed_chars = []
  str.trim().split('').some((c) => {
    if (ALLOWED_STR.indexOf(c) == -1) return true
    passed_chars.push(c)
  })

  const parsedInt = parseInt(passed_chars.join(''))
  if (parsedInt > INT_MAX) return INT_MAX
  if (parsedInt < INT_MIN) return INT_MIN
  if (isNaN(parsedInt)) return 0
  return parsedInt
};

console.log(myAtoi("4193 with words"))
console.log(myAtoi("words and 987"))
console.log(myAtoi("-"))
