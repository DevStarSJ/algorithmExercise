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

const maxOfTwo = (nums, index) => (nums[index] > nums[index + 1]) ? nums[index] : nums[index + 1]

const maxSlidingWindow = (nums, k) => {
  const len = nums.length
  let resultNums = nums
  for (let j = 0; j < k - 1; j++) {
    resultNums = range(0, resultNums.length - 1).map(i => maxOfTwo(resultNums, i))
  }
  return resultNums
};

const nums = [1,3,-1,-3,5,3,6,7]
const k = 4
console.log(maxSlidingWindow(nums, k))