/**
 * @param {string} s
 * @return {number}
 */
const longestValidParentheses = (s) => {
  let openStack = []
  let validCheck = new Array(s.length).fill(0)

  const setValid = (i) => {
    validCheck[i] = 1
    const a = openStack.pop()
    // console.log('openStack.pop() = ',a, openStack )
    validCheck[a] = 1
  }

  for (let i = 0; i < s.length; i++) {
    // console.log(openStack, validCheck)
    const c = s[i]
    if (c == '(') {
      openStack.push(i)
    } else {
      // console.log(i, openStack, openStack.length)
      if (openStack.length > 0) {
        setValid(i)
      } else {
        openStack = []
      }
    }
  }

  // console.log(validCheck)
  
  let maxValidLength = 0
  let currentValidLength = 0

  for (let i = 0; i < validCheck.length; i++) {
    if (validCheck[i] == 0) {
      currentValidLength = 0
    } else {
      currentValidLength += 1
      if (maxValidLength < currentValidLength)
        maxValidLength = currentValidLength
    }
  }

  return maxValidLength
}

const s = "()(())"
console.log(longestValidParentheses(s))