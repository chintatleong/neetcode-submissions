# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        next_digit = 0

        dummy = ListNode()
        curr = ListNode()
        dummy.next = curr

        while l1 and l2:
            curr_digit = (l1.val + l2.val + next_digit) % 10
            next_digit = (l1.val + l2.val) // 10
            curr.val = curr_digit

            if (l1.next == None or l2 == None) and next_digit == 0:
                next_node = None
            elif (l1.next == None or l2 == None) and next_digit == 1:
                next_node = ListNode(1, None)
            else:
                next_node = ListNode()

            curr.next = next_node
            curr = curr.next

            l1 = l1.next
            l2 = l2.next

        if l1:
            curr.next = l1
        
        if l2:
            curr.next = l2

        return dummy.next

        
        