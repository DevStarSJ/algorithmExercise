/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */

const range = (start, k) => {
  let result = []
  for (let i = 0; i < k; i++) {
    result.push(start + i)
  }
  return result
}

const maxSlidingWindow = (nums, k) => {
  const len = nums.length
  let result = []
  for (let i = 0; i < len - k + 1; i++) {
    const subMax = Math.max(...range(i, k).map(pos => nums[pos]))
    result.push(subMax)
  }
  return result
};

const nums = [1,3,-1,-3,5,3,6,7]
const k = 3
console.log(maxSlidingWindow(nums, k))