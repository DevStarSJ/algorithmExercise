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

const arrayToLinkedList = (arr) => {
  let head = new ListNode1(arr[0])
  let current = head
  for (let i = 1; i < arr.length; i++) {
    const newNode = new ListNode1(arr[i])
    current.next = newNode
    current = newNode
  }
  return head
}

const linkedListToArray = (head) => {
  let arr = []
  let current = head
  while (current !== undefined) {
    arr.push(current.val)
    current = current.next
  }
  return arr
}

var deleteDuplicates = (head) => {
  const head1 = arrayToLinkedList(head)
  if (head1.next === undefined) return head1
  let before = head1
  let current = head1.next
  checkList[head1.val] = 1

  while (current !== undefined) {
    if (checkList[current.val] === 0) {
      checkList[current.val] = 1
      before = current
    } else {
      before.next = current.next
    }
    current = current.next
  }
  return linkedListToArray(head1)
};

const arr = [1,1,2,3,3]
// const arr = [3,4,3,6]

console.log(deleteDuplicates(arr))
