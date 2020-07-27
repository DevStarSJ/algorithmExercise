/**
 * @param {string} s
 * @param {string} p
 * @return {boolean}
 */

// T[s][p] =
//    T[s-1][p-1] if s == p or p == .
//    if p == *
//        T[s][p-2]
//        or
//        T[s-1][p] if s == p-1 or p-1 == .          

const display = (matrix) => {
  let m = matrix.map(row => row.map(one => one === true ? 'O' : 'X'))
  m.forEach(row => console.log(row.join('')))
}

const initMatrix = (str, pattern) => {
  const sLen = str.length
  const pLen = pattern.length

  let T = new Array(sLen + 1).fill(false).map(() => new Array(pLen + 1).fill(false))
  T[0][0] = true
  for (let j = 1; j < pLen + 1; j++) {
    if (pattern[j-1] == '*') T[0][j] = T[0][j-2]
  }
  return T
}

const isMatchAt = (s, p) => ((s == p)||(p == '.'))

const isMatch = (str, pattern) => {
  const sLen = str.length
  const pLen = pattern.length
  let T = initMatrix(str, pattern)

  for (let i = 1; i < sLen + 1; i++) {
    for (let j = 1; j < pLen + 1; j++) {
      if (isMatchAt(str[i-1], pattern[j-1]))
        T[i][j] = T[i-1][j-1]
      else if (pattern[j-1] == '*') {
        T[i][j] = T[i][j-2]
        if (!T[i][j] && isMatchAt(str[i-1], pattern[j-2]))
          T[i][j] = T[i-1][j]
      } else
        T[i][j] = false
    }
  }

  return T[sLen][pLen] == true
};

console.log(isMatch('ab', '.*') == true)
console.log(isMatch("a", ".*..") == false)
console.log(isMatch("bbbba", ".*a*a") == true)
console.log(isMatch("aa", "a") == false)
console.log(isMatch("a", "b") == false)
console.log(isMatch('aaa', 'ab*a') == false)
console.log(isMatch('ab', '.*c') == false)
console.log(isMatch('aaa', 'aaaa') == false)
console.log(isMatch('xaabyc', 'xa*b.c') == true)
console.log(isMatch('mississipi', 'mis*is*p*.') == false)
console.log(isMatch('ab', '.*') == true)
