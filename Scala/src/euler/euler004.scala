package euler

object euler004 {
  def main(args: Array[String]) {
    val M = new MathExt()
    var maxNum = 0L
    for (a <- M.numbers(100).takeWhile(_ < 1000);
         b <- M.numbers(100).takeWhile(_ < 1000)) {
      val c = a * b
      if (M.isPalindrome(c) && c > maxNum)
        maxNum = c
    }
    print (maxNum)
  }
}

