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

const initMatrix = (sLen, pLen, pattern) => {
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
  let T = initMatrix(sLen, pLen, pattern)

  // console.log('INIT :')
  // display(T)

  for (let i = 1; i < sLen + 1; i++) {
    for (let j = 1; j < pLen + 1; j++) {
      // console.log('s =',str[i], 'p =', pattern[j], i, j)
      if (isMatchAt(str[i-1], pattern[j-1])) {
        T[i][j] = T[i-1][j-1]
      } else if (pattern[j-1] == '*') {
        // console.log('P[j-1] == * //', 'P[j-2] =', pattern[j-2], i, j)
        if (T[i][j-2] === true) {
          T[i][j] = true
        } else if (isMatchAt(str[i-1], pattern[j-2])) {
          // console.log('T[i-1][j]=', T[i-1][j], i, j, str[i-1], pattern[j-2])
          T[i][j] = T[i-1][j]
        } else {
          T[i][j] = false
        }
      } else {
        T[i][j] = false
      }

    }
    // console.log('ROUND :', i)
    // display(T)
  }

  // console.log('result = ', T[sLen][sLen], pLen, sLen, T)

  return T[sLen][pLen]
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
