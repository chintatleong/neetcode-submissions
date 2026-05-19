# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False

        fast = head.next
        slow = head

        while fast and slow:
            if (fast == slow) and fast != None:
                return True
        
            fast = fast.next
            if fast == None:
                return False

            fast = fast.next
            if fast == None:
                return False
            
            slow = slow.next
        
        return False