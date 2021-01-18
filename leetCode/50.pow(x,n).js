/**
 * @param {number} x
 * @param {number} n
 * @return {number}
 */
const myPow = (x, n) => {
  if (n === 0) return 1
  const signed = n > 0
  const unsigned_n = signed ? n : -n
  const unsigned_result = f1(x, unsigned_n)

  return signed ? unsigned_result : 1.0 / unsigned_result
}

const f1 = (x ,n) => {
  if (n === 1) return x
  if (n === 2) return x * x

  const [quotient, remainder] = devide(n, 2)
  q = f1(x*x, quotient)
  return q * (remainder === 1 ? x : 1)
}

const devide = (a, b) => {
  const quotient = parseInt(a / b)
  const remainder = a % b
  return [quotient, remainder]
}
