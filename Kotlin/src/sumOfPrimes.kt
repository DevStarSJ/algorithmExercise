fun sumOfPrimes(limit: Int): Long {
   val seq: Sequence<Long> = sequenceOf(2L) +
           generateSequence(3L,{ it + 2 }).takeWhile { it < limit }

    fun isPrime(n: Long): Boolean = seq.takeWhile { it * it <= n }.all { n % it != 0L }

    return seq.filter(::isPrime).sum()
}

fun main() {
    println(sumOfPrimes(10))
}