/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function(l1, l2, carry = 0) {
  if (l1 == null && l2 == null) {
      if (carry == 0) return null
      return new ListNode(carry, null)
  }
  
  const l1Val = l1 ? l1.val : 0
  const l2Val = l2 ? l2.val : 0
  const l1Next = l1 ? l1.next : null
  const l2Next = l2 ? l2.next : null
  const value = l1Val + l2Val + carry
  let node = new ListNode(value % 10)
  node.next = addTwoNumbers(l1Next, l2Next, value >= 10 ? 1 : 0)
  return node
};