# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # no cycle, last node points to null
        # if cycle, last node index will set to ith index
        # variable index determubes the beginning of the cycle (not given)
        copy = head

        while head:
            head = head.next
            copy = copy.next.next

            if head == None or copy == None:
                return False

            if head.next != None and copy == head:
                return True

        return False 