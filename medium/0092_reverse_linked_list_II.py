# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        prev = None
        curr = head

        # move up until the m-th node
        for _ in range(m-1):
            prev = curr
            curr = curr.next

        # remember before_start and start
        before_start = preacv
        start = curr

        # move up one
        prev = curr
        curr = curr.next

        for _ in range(n-m):
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        # here, curr is the node after the last node
        # prev is the last node in the range to reverse
        start.next = curr

        if before_start:
            before_start.next = prev
        else:
            head = prev

        return head
