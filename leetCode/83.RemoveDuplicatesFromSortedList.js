/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
class ListNode1 {
  constructor(val, next) {
      this.val = val
      this.next = (next === undefined ? undefined : next)
  }
}

let checkList = new Array(1001).fill(0)

var deleteDuplicates = (head) => {
  // const head = arrayToLinkedList(head)
  if (head.next === undefined) return head
  let before = head
  let current = head.next
  checkList[head.val] = 1

  while (current !== undefined) {
    if (checkList[current.val] === 0) {
      checkList[current.val] = 1
      before = current
    } else {
      before.next = current.next
    }
    current = current.next
  }
  return head//linkedListToArray(head)
};

const arr = [1,1,2,3,3]
// const arr = [3,4,3,6]

console.log(deleteDuplicates(arr))

// const arrayToLinkedList = (arr) => {
//   let head = new ListNode1(arr[0])
//   let current = head
//   for (let i = 1; i < arr.length; i++) {
//     const newNode = new ListNode1(arr[i])
//     current.next = newNode
//     current = newNode
//   }
//   return head
// }

// const linkedListToArray = (head) => {
//   let arr = []
//   let current = head
//   while (current !== undefined) {
//     arr.push(current.val)
//     current = current.next
//   }
//   return arr
// }

// LeetCode에 제출한 코드
/* 
var deleteDuplicates = (head) => {
  if (head == null) return head
  if (head.next === null) return head
    
  let checkList = new Array(2001).fill(0)

  let before = head
  let current = head.next
  checkList[head.val+100] = 1

  while (current !== null) {
    if (checkList[current.val+100] === 0) {
      checkList[current.val+100] = 1
      before = current
    } else {
      before.next = current.next
    }
    current = current.next
  }
  return head
};
*/