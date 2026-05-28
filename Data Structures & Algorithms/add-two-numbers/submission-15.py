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

        while l1 or l2 or next_digit:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            curr_digit = (v1 + v2 + next_digit) % 10
            next_digit = (v1 + v2 + next_digit) // 10

            if (l1 == None or l2 == None):
                if (l1 == None and l2.next == None):
                    if (next_digit == 1):
                        next_node = ListNode(1, None)
                elif (l1.next == None and l2 == None):
                    if (next_digit == 1):
                        next_node = ListNode(1, None)
                else:
                    next_node = ListNode()
            elif (l1.next == None and l2.next == None) and next_digit == 0:
                next_node = None
            elif (l1.next == None or l2.next == None) and next_digit == 1:
                next_node = ListNode(1, None)
            else:
                next_node = ListNode()

            curr.val = curr_digit
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

        
        