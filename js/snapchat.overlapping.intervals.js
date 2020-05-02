function overlappingIntervals(intervals) {
  intervals = sortIntervalsByFirstElement(intervals)
  intervals = mergeIntervalsInOverlapping(intervals)
  return intervals
}

// n lon n
function sortIntervalsByFirstElement(intervals) {
  return intervals.sort((a, b) => a[0] - b[0])
}

// n
function mergeIntervalsInOverlapping(intervals) {
  let result = []

  intervals.forEach((interval, i) => {
    if (result.length === 0) {
      result.push(interval)
      return
    }

    if (interval[0] < result[result.length - 1][1]) {
      const left = result.pop()
      interval = [
        Math.min(interval[0], left[0]),
        Math.max(interval[1], left[1]),
      ]
    }
    result.push(interval)
  })

  return result
}

// test

const a = [
  [1, 3],
  [5, 8],
  [4, 10],
  [20, 25],
]
console.log(overlappingIntervals(a))

const b = [
  [1, 3],
  [2, 4],
  [3, 10],
  [20, 30],
  [10, 20],
]

console.log(overlappingIntervals(b))
