# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None:
            return False

        slow = fast = head

        while True:
            # move the fast pointer
            if fast.next is None:
                return False
            if fast.next.next is None:
                return False

            fast = fast.next.next

            # move the slow pointer
            slow = slow.next

            if fast == slow:
                return True
