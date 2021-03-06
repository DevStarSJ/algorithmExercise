/**
 * @param {number[]} height
 * @return {number}
 */

const area = (a, b) => (b[0] - a[0]) * Math.min(a[1],b[1])

const maxArea = (heights) => {
  const points = heights.map( (h, i) => [i, h])
  let left = 0
  let right = points.length -1

  let maximum = 0
  while(left < right) {
    maximum = Math.max(maximum, area(points[left], points[right]))
    if (points[left][1] > points[right][1])
      right--
    else
      left++
  }
  return maximum
};

console.log(maxArea([1,2,4,3]) == 4)
console.log(maxArea([1,8,6,2,5,4,8,3,7]) == 49)