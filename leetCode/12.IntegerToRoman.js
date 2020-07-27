/**
 * @param {number} num
 * @return {string}
 */

const divide = (num, divisor) => {
  const quotient = parseInt(Math.floor(num / divisor), 10)
  const remainder = num % divisor
  return { quotient, remainder}
}

const toRoman = (divisor, letter) => (num) => {
  const { quotient, remainder } = divide(num, divisor);
  return {
    roman: letter.repeat(quotient),
    remainder
  }
}

const toRomans = [[1000, 'M'], [900, 'CM'], [500, 'D'], [400, 'CD'], [100, 'C'], [90, 'XC'], [50, 'L'], [40, 'XL'], [10, 'X'], [9, 'IX'], [5, 'V'], [4, 'IV'], [1, 'I']]
                .map(([divisor,letter]) => toRoman(divisor, letter))

const intToRoman = (num) => {
  let resultRoman = ''
  let currentReminder = num
  toRomans.forEach(toRoman => {
    const { roman, remainder } = toRoman(currentReminder)
    resultRoman += roman
    currentReminder = remainder
  })
  return resultRoman
};

console.log(intToRoman(17))
