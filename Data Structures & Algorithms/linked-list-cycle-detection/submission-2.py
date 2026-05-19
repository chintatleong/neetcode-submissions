# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head

        if (fast.next.next == None and slow.next.next == None):
            return False

        while fast and slow:
            if (fast == slow):
                return True
        
            fast = fast.next.next
            slow = slow.next
        
        return False