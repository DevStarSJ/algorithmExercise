/**
 * @param {number[]} height
 * @return {number}
 */

const area = (a, b) => Math.abs(a[0] - b[0]) * Math.min(a[1],b[1])

const maxArea = (heights) => {
  const points = heights.map( (h, i) => [i, h])
  let maximum = 0
  for (let i = 0; i < points.length; i++) {
    for (let j = i+1; j < points.length; j++) {
      maximum = Math.max(maximum, area(points[i], points[j]))
    }
  }
  return maximum
};

console.log(maxArea([1,8,6,2,5,4,8,3,7]) == 49)