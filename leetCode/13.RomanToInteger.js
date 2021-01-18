/**
 * @param {string} s
 * @return {number}
 */

const values = {
  I: 1,
  V: 5,
  X: 10,
  L: 50,
  C: 100,
  D: 500,
  M: 1000
}

const romanToInt = (s) => {
  let result = 0

  for (let i = 0; i < s.length; i++) {
    const e = s[i]
    if (i === s.length - 1) {
      result += values[e]
      return result 
    }
    
    if (values[e] < values[s[i+1]]) {
      result += values[s[i+1]] - values[e]
      i++
    } else {
      result += values[e]
    }
  }
  return result
}