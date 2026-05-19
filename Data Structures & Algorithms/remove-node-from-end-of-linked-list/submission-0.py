# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        count = 0


        while curr:     # count how many nodes
            curr = curr.next
            count += 1

        stop = count - n    # when to stop 

        prev = None
        curr = head
        i = 0

        while curr: 
            if (i == stop):
                if (prev == None):
                    return None
                prev.next = curr.next

            prev = curr
            curr = curr.next
            i += 1

        return head
            
