package euler

import scala.math.max

class CollectionExt {

  private val M = new MathExt()

  def toCountMap[T](list: List[T]): Map[T, Int] = {
    return list.groupBy(identity).mapValues(_.size)
  }

  def mergeToMaxValue[T](list: List[Map[T, Int]]) : scala.collection.mutable.Map[T, Int] = {
    var result = scala.collection.mutable.Map[T, Int]()

    list.foreach{one => {
      one.foreach{ case(key:T, value:Int) => {
        if (result.contains(key)) {
          result(key) = max(result(key), value)
        } else {
          result += (key -> value)
        }
      }}
    }}

    return result
  }
}
