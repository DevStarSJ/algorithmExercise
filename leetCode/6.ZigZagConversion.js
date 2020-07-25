/**
 * @param {string} s
 * @param {number} numRows
 * @return {string}
 */

 // 수열 : N + (N-2)
 // 3 -> 4
 // 4 -> 6
 // 5 -> 8
 // 0 ~ N-1 -> (0, i)
 // N ~ end -> (i-N, N-i)
 // 4 -> 4 - 1
 // 5 -> 5 - 2
const convert = (s, numRows) => {
  if (s.length < 3) return s
  if (numRows == 1) return s

  const seqUnit = numRows * 2 - 2
  const len = s.length
  let matrix = new Array(numRows).fill('').map(() => new Array(Math.floor(len / seqUnit) * numRows).fill(''))

  console.log('seqUnit =', seqUnit, 'numRows =', numRows)

  for (let i = 0; i < len; i++) {
    const seqIndex = i % seqUnit
    const seqTimes = Math.trunc(i / seqUnit)
    const baseX = seqTimes * (numRows - 1)
    // console.log(i, seqIndex, seqTimes, baseX, s[i])
    if (seqIndex < numRows) {
      const x = baseX
      const y = seqIndex
      matrix[y][x] = s[i]
    } else {
      const x = baseX + seqIndex - numRows + 1
      const y = numRows - (seqIndex - numRows + 2)
      // console.log(x, y, i, s[i])
      matrix[y][x] = s[i]
    }
    // console.log(matrix)
  }
  return matrix.map(row => row.filter(one => one != '').join('')).join('')
};

console.log(convert("PAYPALISHIRING", 4))
console.log(convert('', 1))
console.log(convert('ABC', 1))