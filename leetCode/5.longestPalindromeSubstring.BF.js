const isPalindrome = (str, i, j) => {
  if (i >= j) return true
  if (str[i] == str[j]) return isPalindrome(str, i+1, j-1)
  return false
}

const longestPalindrome = (str) => {
  const len = str.length
  let bestI = undefined
  let bestJ = undefined
  let bestLen = 0
  for (let i = 0; i < len; i++) {
    for (let j = len -1; j >= i; j--) {
      // console.log(i, j, bestLen, str.substring(i, j+1), isPalindrome(str, i, j))
      if ((j - i + 1) < bestLen) break;
      if (isPalindrome(str, i, j)) {
        bestLen = j - i + 1
        bestI = i
        bestJ = j
      }
    }
  }

  return str.substring(bestI, bestJ+1)
}

console.log(longestPalindrome("babad"))
console.log(longestPalindrome("aaaabbaa"))