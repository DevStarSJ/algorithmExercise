/**
 * @param {number} x
 * @return {number}
 */
const reverse = (x) => {
  let s = x.toString()
  let sign = ''
  if (s[0] == '-') {
    sign = '-'
    s = s.substring(1, s.length)
  }
  const answer = parseInt(`${sign}${s.split('').reverse().join('')}`)
  const limitInt = Math.pow(2, 31)
  return -1 * limitInt <= answer && answer <= limitInt ? answer : 0 
};

console.log(reverse(123))
console.log(reverse(-123))
console.log(reverse(120))
