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

        while l1 or l2:
            if (l1 == None and l2 != None):
                curr_digit = (l2.val + next_digit) % 10
                next_digit = (l2.val + next_digit) // 10

            elif (l1 != None and l2 == None):
                curr_digit = (l1.val + next_digit) % 10
                next_digit = (l1.val + next_digit) // 10
            else:
                curr_digit = (l1.val + l2.val + next_digit) % 10
                next_digit = (l1.val + l2.val + next_digit) // 10
            
            curr.val = curr_digit

            if (l1.next == None or l2 == None) and next_digit == 0:
                next_node = None
            elif (l1.next == None or l2 == None) and next_digit == 1:
                next_node = ListNode(1, None)
            else:
                next_node = ListNode()

            curr.next = next_node
            curr = curr.next

            if (l1 == None and l2 != None):
                l2 = l2.next
            elif (l1 != None and l2 == None):
                l1 = l1.next
            else:
                l1 = l1.next
                l2 = l2.next

        return dummy.next

        
        