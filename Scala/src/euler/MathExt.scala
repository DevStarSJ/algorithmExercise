package euler

class MathExt {

  def isDivisible(n: Long, b: Long): Boolean = n % b == 0        // n은 b로 나누어지는가
  def isMultiple (b: Long)(n: Long): Boolean = isDivisible(n, b) // b는 n의 약수인가
  def isDivisor  (n: Long)(b: Long): Boolean = isDivisible(n, b) // n은 b의 배수인가

  def isEven(n: Long): Boolean = isMultiple(2)(n)
  def isOdd( n: Long): Boolean = !isEven(n)

  def fibonacciSequence(a: Long = 0, b: Long = 1): Stream[Long] = a #:: fibonacciSequence(b, a + b)

  def numbers   (a: Long = 0): Stream[Long] = a #:: numbers   (a+1)
  def numbersRev(a: Long)    : Stream[Long] = a #:: numbersRev(a-1)

  def isPrime(n: Long): Boolean = {
    if (n  < 2)    return false
    if (n == 2)    return true
    if (isEven(n)) return false

    for(i <- numbers(3).takeWhile(a => (a * a) <= n) if isDivisor(n)(i)) return false

    return true
  }

  def getDivisors(n: Long): List[Long] = {
    if (n < 1) return List[Long]()
    if (n == 1) return List[Long](1)
    var devisors = List[Long](1, n)
    var i = 2L
    var end = n - 1

    while (i < end) {
      if (isDivisible(n, i)) {
        end = n / i
        devisors = devisors :+ i
        if (end != i) devisors = devisors :+ end
      }
      i += 1
    }

    return devisors.sorted
  }

  def isPalindrome(n: Long): Boolean = {
    val s = n.toString
    return s == s.reverse
  }

  def doPrimeFactorization(n: Long): List[Long] = {
    if (n < 2) return List[Long](n)
    var end = n
    var result = List[Long]()
    while (!isPrime(end)) {
      val a: Long = numbers(2).takeWhile(_ <= end).filter(isPrime).filter(isDivisible(end, _)).take(1).max
      result = result :+ a
      end = end / a
    }

    return result :+ end
  }
}