package euler
import scala.math.{pow}

object euler005 {
  def main(args: Array[String]) {
    val M = new MathExt()
    val C = new CollectionExt()

    val value = C.mergeToMaxValue(M.numbers(1).takeWhile(_ <= 20)
                  .map(M.doPrimeFactorization)
                  .map(C.toCountMap)
                  .toList).toList
                .map(e => (pow(e._1, e._2)).toLong)
                .reduce((a, b) => a * b)

    print(value)
  }
}

