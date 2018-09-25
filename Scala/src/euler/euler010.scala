package euler

object euler010 {
  def main(args: Array[String]) {
    val M = new MathExt()

    println(M.numbers(2).takeWhile(_ <= 2000000).filter(M.isPrime).sum)
  }
}
