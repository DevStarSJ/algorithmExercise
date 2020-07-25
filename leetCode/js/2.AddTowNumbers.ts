/**
 * Definition for singly-linked list.
 * class ListNode {
 *     val: number
 *     next: ListNode | null
 *     constructor(val?: number, next?: ListNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */

const toList = (listNode: ListNode | null) => {
  if (listNode === null) return [0] 
  let numList = []
  let currentNode = listNode
  while(true) {
      numList.push(currentNode.val)
      if (currentNode.next == null) break
      currentNode = currentNode.next
  }
  return numList
}

const listNodeToNumber = (listNode: ListNode | null) => {
  if (listNode == null) return '0' 
  return toList(listNode).reverse().map(n => `${n}`).join('')
}

const numberToListNode = (num: string) => {
  let node: ListNode | null  = null
  num.split('').forEach(i => {
      const newNode = new ListNode(parseInt(i), node)
      node = newNode
  })
  return node
}

const plusTwoNumericString = (a: string, b: string) => {
  const aList = a.split('').reverse()
  const bList = b.split('').reverse()
  const answer = []
  let carry = 0
  for (let i = 0; i < Math.max(aList.length, bList.length); i++) {
    const aOne = aList[i] || '0'
    const bOne = bList[i] || '0'
    let value = parseInt(aOne) + parseInt(bOne) + carry
    carry = 0
    if (value >= 10) {
      carry = 1
      value -= 10
    }
    answer.push(value)
  }
  if (carry == 1) answer.push('1')
  return answer.reverse().join('')
  
}

function addTwoNumbers(l1: ListNode | null, l2: ListNode | null): ListNode | null {
  const num1 = listNodeToNumber(l1)
  const num2 = listNodeToNumber(l2)
  const num3 = plusTwoNumericString(num1,  num2)
  // console.log(num1, num2, num3)
  return numberToListNode(num3)
};