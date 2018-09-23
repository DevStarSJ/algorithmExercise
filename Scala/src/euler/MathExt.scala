package euler

class MathExt {

  // 배수 : number가 base의 배수인가 ?
  def isDivisible(n: Long, b: Long): Boolean = n % b == 0
  def isMultiple (b: Long)(n: Long): Boolean = isDivisible(n, b)
  def isDevisor  (n: Long)(b: Long): Boolean = isDivisible(n, b)

  def isEven(n: Long): Boolean = isMultiple(2)(n)
  def isOdd(n: Long): Boolean = !isEven(n)

  def fibonacciSequence(a: Long = 0, b: Long = 1): Stream[Long] = a #:: fibonacciSequence(b, a + b)

  def numbers(a: Long = 0): Stream[Long] = a #:: numbers(a+1)

  def isPrime(n: Long): Boolean = {
    if (n == 1l)
      return false
    if (n == 2l)
      return true

    //val a = numbers(3).takeWhile(a => (a * a) < n).filter(isDevisor(n)).toArray.count





  }
}