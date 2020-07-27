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
        if (isExist(n3)) continue
        if (n3.reduce((a,b) => a+b) == 0) {
          result.push(n3)
        }
      }
    }
  }
  return result.filter(unique)
};

console.log(threeSum([-1,0,1,2,-1,-4]))