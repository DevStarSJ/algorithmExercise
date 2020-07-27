/**
 * @param {number[]} nums
 * @return {number[][]}
 */
const unique = (num, i, self) => self.indexOf(num) === i

const threeSum = (nums) => {
  const sorted = nums.sort((a,b) => a-b)
  let result = []

  const isExist = (n3) => {
    return result.some((triple) => {
      if (n3[0] == triple[0] && n3[1] == triple[1] && n3[2] == triple[2]) return true
      return false
    })
  }

  for (let i = 0; i < nums.length; i++) {
    for (let j = i+1; j < nums.length; j++) {
      for (let k = j+1; k < nums.length; k++) {
        const n3 = [nums[i], nums[j], nums[k]].sort((a,b) => a-b)
        if (n3.reduce((a,b) => a+b) == 0) {
          if (!isExist(n3))
            result.push(n3)
        }
      }
    }
  }
  return result.filter(unique)
};

// console.log(threeSum([-1,0,1,2,-1,-4]))

// const nums = [-4,-8,7,13,10,1,-14,-13,0,8,6,-13,-5,-4,-12,2,-11,7,-5,0,-9,-14,-8,-9,2,-7,-13,-3,13,9,-14,-6,8,1,14,-5,-13,8,-10,-5,1,11,-11,3,14,-8,-10,-12,6,-8,-5,13,-15,2,11,-5,10,6,-1,1,0,0,2,-7,8,-6,3,3,-13,8,5,-5,-3,9,5,-4,-14,11,-8,7,10,-6,-3,11,12,-14,-9,-1,7,5,-15,14,12,-5,-8,-2,4,2,-14,-2,-12,6,8,0,0,-2,3,-7,-14,2,7,12,12,12,0,9,13,-2,-15,-3,10,-14,-4,7,-12,3,-10]
const nums = [-1,-12,14,-6,4,-11,2,-7,13,-15,-1,11,-15,-15,13,-9,-11,-10,-7,-13,7,9,-13,-3,10,1,-5,12,11,-9,2,-4,-6,-7,5,5,-2,14,13,-12,14,-3,14,14,-11,5,12,-6,10,-9,-4,-6,-15,-9,-1,2,-1,9,-9,-5,-15,8,-2,-6,9,10,7,14,9,5,-13,9,-12,8,8,-8,-2,-2,1,-15,-4,5,-13,-4,3,1,5,-13,-13,11,-11,10,5,3,11,-9,-2,3,-10,-7,-6,14,9,-11,7,2,-4,13,7,5,13,-12,-13,7,-9,5,-7,11,-1,-12,8,3,13,-10,13,1,-4]
console.log(threeSum(nums))
