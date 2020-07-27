/**
 * @param {string[]} strs
 * @return {string}
 */
const longestCommonPrefix = (strs) => {
  if (strs.length == 0) return ''
  let commonPrefix = ''
  let minLen = Math.min(...strs.map(str => str.length))

  for (let i = 0; i < minLen; i++) {
    const sameChar = strs.map(str => str[i]).reduce((a,b) => a == b ? a : undefined)
    if (sameChar == undefined) return commonPrefix
    commonPrefix += sameChar
  }
  return commonPrefix
}

console.log(longestCommonPrefix(["flower", "flow", "flight"]))
console.log(longestCommonPrefix(["dog","racecar","car"]))
