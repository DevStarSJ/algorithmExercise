package euler

object ex003 {
  def main(args: Array[String]) {
    val M = new MathExt()

    //(1l to 600851475143l).filter(M.isDevisor(600851475143l)).filter()

     println(M.numbers().takeWhile(_ < 600851475143l).toList)

//    println(M.fibonacciSequence()
//      .takeWhile(_ < 4000000)
//      .toList
//      .filter(M.isEven)
//      .sum)
  }
}
