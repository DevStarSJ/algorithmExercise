/**
 * @param {string} s
 * @param {string} p
 * @return {boolean}
 */

const patternSplit = (pattern) => pattern.split('').map((w, i) => pattern[i+1] == '*' ? `${w}*` : w).filter(w => w != '*')

const matchableIndexes = (str, sPos, matchChar) => {
  let matchableIndexes = [sPos]

  const isContinue = (i) => {
    if (i>= str.length) return false
    if (matchChar == '.') return true
    return str[i] == matchChar
  }

  for (let i = sPos; isContinue(i); i++) {
    matchableIndexes.push(i+1)
  }
  return matchableIndexes
}

const isMatchAt = (str, patterns, sPos, pPos) => {
  // console.log('isMatchAt', str, patterns, sPos, pPos)
  if (str[sPos] == undefined && patterns[pPos] == undefined) return true
  if (str[sPos] != undefined && patterns[pPos] == undefined) {
    // console.log('str[sPos] != undefined && patterns[pPos] == undefined')
    return false
  }
  if (str[sPos] == undefined && patterns[pPos] != undefined && patterns[pPos].length == 1) {
    // console.log('str[sPos] == undefined && patterns[pPos] != undefined && patterns[pPos].length == 1')
    return false
  }
  if (patterns[pPos] == '.' && str[sPos] != undefined) return isMatchAt(str, patterns, sPos+1, pPos+1)
  if (patterns[pPos] == str[sPos]) return isMatchAt(str, patterns, sPos+1, pPos+1)

  if (patterns[pPos].length == 2) {
    if (str[sPos] == undefined) return isMatchAt(str, patterns, sPos, pPos+1)
    const matchChar = patterns[pPos][0]
    // console.log('matchChar=',matchChar)
    if (str[sPos] != matchChar && matchChar != '.') return isMatchAt(str, patterns, sPos, pPos+1)
    // console.log(matchableIndexes(str, sPos, matchChar))
    return matchableIndexes(str, sPos, matchChar).some(i => {
      return isMatchAt(str, patterns, i, pPos+1)
    })
  }
  return false
}

const isMatch = (s, p) => {
  const patterns = patternSplit(p);
  // console.log(patterns)
  return isMatchAt(s, patterns, 0, 0)
};

console.log(isMatch("a", "b") == false)
console.log(isMatch("bbbba", ".*a*a") == true)
console.log(isMatch('aaa', 'ab*a') == false)
console.log(isMatch('ab', '.*c') == false)
console.log(isMatch('aaa', 'aaaa') == false)
console.log(isMatch('ab', '.*') == true)
console.log(isMatch('xaabyc', 'xa*b.c') == true)
console.log(isMatch('mississipi', 'mis*is*p*.') == false)