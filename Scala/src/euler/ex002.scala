package euler

object ex002 {
  def main(args: Array[String]) {
    val M = new MathExt()

    println(M.fibonacciSequence()
             .takeWhile(_ < 4000000)
             .toList
             .filter(M.isEven)
             .sum)
  }
}
