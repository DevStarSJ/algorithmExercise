package euler

object euler003 {
  def main(args: Array[String]) {
    val M = new MathExt()
    println(M.getDivisors(600851475143L).filter(M.isPrime).max)
  }
}
