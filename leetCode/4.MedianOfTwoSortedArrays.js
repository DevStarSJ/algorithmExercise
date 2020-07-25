/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var findMedianSortedArrays = function(nums1, nums2) {
  const nums = nums1.concat(nums2).sort((a, b) => a - b)
  if (nums.length % 2 === 1) return nums[((nums.length-1)/2)]
  return (nums[nums.length/2-1] + nums[nums.length/2])/2
};

console.log(findMedianSortedArrays([3], [-2,-1]))