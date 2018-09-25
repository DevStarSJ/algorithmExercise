package euler

object euler005 {
  def main(args: Array[String]) {
    val M = new MathExt()

    println(M.doPrimeFactorization(20))

//    def isAllDevisors(nums: List[Long])(base: Long): Boolean = {
//      val isDivisorBase = M.isDivisor(base)(_)
//      for (i <- nums if !isDivisorBase(i)) return false
//      return true
//    }
//
//    val hasAllDevisorsUnder20 = isAllDevisors(M.numbers(1).takeWhile(_ <= 20).toList)(_)
//
//    def getMinAnswer(): Long = {
//      for (n <- M.numbers(21)) {
//        println(n)
//        if (hasAllDevisorsUnder20(n)) return n
//      }
//      return Long.MaxValue
//    }
//
//    println(getMinAnswer())
  }
}

