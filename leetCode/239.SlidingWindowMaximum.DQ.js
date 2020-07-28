/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */

class Deque {
  array = []
  push = (val) => this.array.push(val)
  peekBack = () => this.array[this.array.length - 1]
  peekFront = () => this.array[0]
  pop = () => this.array.pop()
  shift = () => this.array.shift()
  isEmpty = () => this.array.length == 0
}

const maxSlidingWindow = (nums, k) => {
  const len = nums.length
  if (len * k == 0) return []
  if (k == 1) return nums

  const Q = new Deque()

  const clear = (i) => {
    if (!Q.isEmpty() && (Q.peekFront() == i - k)) Q.shift()

    while (!Q.isEmpty() && nums[Q.peekBack()] < nums[i]) {
      Q.pop()
    }
  }


  for (let i = 0; i < k; i++) {
    clear(i)
    Q.push(i)
  }
  
  let resultNums = [nums[Q.peekFront()]]

  const debug = () => console.log(Q.array, Q.array.map(n => nums[n]))

  // debug()

  for (let i = k; i < len; i++) {
    // console.log('before clear', k, i, nums[i])
    // debug()    
    clear(i)
    Q.push(i)
    // console.log('after clear')
    // debug()    
    resultNums.push(nums[Q.peekFront()])
  }

  return resultNums
};

// const nums = [1,3,-1,-3,5,3,6,7]
// const k = 3

const nums = [7,2,4]
const k = 2

console.log(maxSlidingWindow(nums, k))