package euler

object euler009 {
  def main(args: Array[String]) {
    val M = new MathExt()

    for (c <- M.numbersRev(997).takeWhile((_ > 2));
         b <- M.numbersRev(c - 1).takeWhile(_ > 1) if 1000 < b + b + c && 1000  > b + c;
         a <- List(1000-b-c)) {
      if (a * a + b * b - c * c == 0) {
        println(a, b, c)
        println(a * b * c)
      }
    }
  }
}
