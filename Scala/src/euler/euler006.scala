package euler

object euler006 {
  def main(args: Array[String]) {
    val M = new MathExt()

    val maxValue = 100

    val squareSum = M.numbers(1).takeWhile(_ <= maxValue).map(a => a*a).sum
    val sum = M.numbers(1).takeWhile(_ <= maxValue).sum
    val sumSquare = sum * sum
    print(sumSquare - squareSum)
  }
}
