/**
 * @param {number[]} nums
 * @return {number[][]}
 */

 const isEqual = (a,b) => {
  for (let i = 0; i < b.length; i++) {
    if (b[i] !== a[i]) return false
  }
  return true
 }

const isExist = (list, newNums) => {
  if (list.length === 0) return false
  for (let i = 0; i < list.length; i++) {
    if (isEqual(list[i], newNums)) return true
  }
  return false
}

const threeSum = (nums) => {
  const sortedNums = nums.sort((a,b) => a-b)
  // console.log(sortedNums)

  const minNum = sortedNums[0]
  const maxNum = sortedNums[nums.length-1]
  // console.log(maxNum, minNum)

  let result = []

  for (let i = 0; i < sortedNums.length - 2; i++) {
    if (i > 0 && nums[i] === nums[i-1]) continue
    for (let j = i+1; j < sortedNums.length -1; j++) {
      const ij = sortedNums[i] + sortedNums[j]
      // console.log('i,j,ij', sortedNums[i], sortedNums[j], ij, ij < minNum || maxNum < ij)
      if (ij < maxNum * -1 || minNum * -1 < ij) continue
      for (let k = j+1; k < sortedNums.length; k++) {
        if (sortedNums[k] + ij === 0) {
          const newNums = [sortedNums[i], sortedNums[j], sortedNums[k]]
          // console.log(result, newNums, isExist(result, newNums))
          if (!isExist(result, newNums)) {
            result.push([sortedNums[i], sortedNums[j], sortedNums[k]])
            break
          }
        }
      }
    }
  }

  return result
}

// console.log(threeSum([-1,0,1,2,-1,-4]))

// const nums = [-4,-8,7,13,10,1,-14,-13,0,8,6,-13,-5,-4,-12,2,-11,7,-5,0,-9,-14,-8,-9,2,-7,-13,-3,13,9,-14,-6,8,1,14,-5,-13,8,-10,-5,1,11,-11,3,14,-8,-10,-12,6,-8,-5,13,-15,2,11,-5,10,6,-1,1,0,0,2,-7,8,-6,3,3,-13,8,5,-5,-3,9,5,-4,-14,11,-8,7,10,-6,-3,11,12,-14,-9,-1,7,5,-15,14,12,-5,-8,-2,4,2,-14,-2,-12,6,8,0,0,-2,3,-7,-14,2,7,12,12,12,0,9,13,-2,-15,-3,10,-14,-4,7,-12,3,-10]
// const nums = [-1,-12,14,-6,4,-11,2,-7,13,-15,-1,11,-15,-15,13,-9,-11,-10,-7,-13,7,9,-13,-3,10,1,-5,12,11,-9,2,-4,-6,-7,5,5,-2,14,13,-12,14,-3,14,14,-11,5,12,-6,10,-9,-4,-6,-15,-9,-1,2,-1,9,-9,-5,-15,8,-2,-6,9,10,7,14,9,5,-13,9,-12,8,8,-8,-2,-2,1,-15,-4,5,-13,-4,3,1,5,-13,-13,11,-11,10,5,3,11,-9,-2,3,-10,-7,-6,14,9,-11,7,2,-4,13,7,5,13,-12,-13,7,-9,5,-7,11,-1,-12,8,3,13,-10,13,1,-4]
// const nums = [-1,0,1,2,-1,-4]
// const nums = [3,0,-2,-1,1,2]
// const nums = [-1,0,1,2,-1,-4,-2,-3,3,0,4]
const nums = [-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]
console.log(threeSum(nums))
