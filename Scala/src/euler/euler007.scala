package euler

object euler007 {
  def main(args: Array[String]) {
    val M = new MathExt()

    print(M.numbers(2).filter(M.isPrime).take(10001).max)
  }
}
