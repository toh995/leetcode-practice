/*
https://leetcode.com/problems/add-two-numbers/

You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
*/

/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */

var divide = function(dividend, divisor) {
    return {
        quotient: Math.floor(dividend / divisor),
        remainder: dividend % divisor,
    };
}

/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function(l1, l2) {
    let currNode1 = l1;
    let currNode2 = l2;
    
    // initialize first value for firstRetNode
    const sum = currNode1.val + currNode2.val;
    const { quotient, remainder } = divide(sum, 10);
    
    let carryover = quotient;
    
    // firstRetNode will the final value that is returned
    let firstRetNode = new ListNode(remainder);
    let currRetNode = firstRetNode;
    
    while (currNode1.next || currNode2.next) {
        // move the currNodes up
        currNode1 = currNode1.next || new ListNode();
        currNode2 = currNode2.next || new ListNode();
        
        currRetNode.next = new ListNode();
        currRetNode = currRetNode.next;
        
        const sum = currNode1.val + currNode2.val + carryover;
        const { quotient, remainder } = divide(sum, 10);
                
        currRetNode.val = remainder;
        carryover = quotient;
    }
    
    // if there is still carryover, continue adding to currRetNode
    while (carryover > 0) {
        currRetNode.next = new ListNode();
        currRetNode = currRetNode.next;
        
        const { quotient, remainder } = divide(carryover, 10);
        
        currRetNode.val = remainder;
        carryover = quotient;
    }
    
    return firstRetNode;
};