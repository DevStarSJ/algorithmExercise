package euler

object ex001 {
  def main(args: Array[String]) {
    val M = new MathExt()

    val x = (1l to 999l)
    val y3 = x.filter(M.isMultiple(3l)).toArray
    val y5 = x.filter(M.isMultiple(5l)).toArray
    val y = (y3 ++ y5).toSet.toArray.sorted
    println(y.sum)
  }
}