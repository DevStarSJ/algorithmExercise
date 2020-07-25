/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */

const present = val => val !== undefined

const twoSum = (nums, target) => {
    let result = []
    nums.some((num, i) => {
        const rightIndex = nums.map((num2, j) => {
            if (i == j) return undefined
            if (num + num2 === target) return j
        }).filter(present)
        if (rightIndex.length === 1) {
            result = [i, rightIndex[0]]
            return true
        }
    })
    return result
};