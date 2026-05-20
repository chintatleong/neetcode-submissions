# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        next_digit = 0

        dummy = ListNode()
        curr = dummy

        while l1 or l2 or next_digit:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            curr_digit = (v1 + v2 + next_digit) % 10
            next_digit = (v1 + v2 + next_digit) // 10

            curr.next = ListNode(curr_digit)

            curr = curr.next

            if l1:
                l1 = l1.next

            if l2:
                l2 = l2.next

        return dummy.next

        
        