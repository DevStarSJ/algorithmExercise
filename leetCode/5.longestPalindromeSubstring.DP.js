const longestPalindrome = (str) => {
  const strLen = str.length
  let matrix = new Array(strLen).fill(0).map(() => new Array(strLen).fill(0))

  let bestLen = 0
  let bestStr = ""

  const setMatrix = (len, i, j) => {
    matrix[i][j] =len
    if (len > bestLen) {
      bestLen = len
      bestStr = str.substring(i, j+1)
    }
  }

  for (let len = 1; len <= strLen; len++) {
    for (let i = 0; i + len <= strLen; i++) {
      const j = i + len - 1
      if (len == 1) {
        setMatrix(len, i, j)
        continue
      }

      if (str[i] != str[j]) {
        matrix[i][j] = 0
        continue
      }

      if (len == 2) {
        setMatrix(len, i, j)
        continue
      }
      
      if (matrix[i+1][j-1] > 0) {
        setMatrix(len, i, j)
      }
    }
  }
  console.log(matrix.map(row => row.map(i => `${i}`).join('')))

  return bestStr
}

console.log(longestPalindrome("babad"))
console.log(longestPalindrome("aaaabbaa"))