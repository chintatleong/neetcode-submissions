# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # two pointer, one at 0 and one at 6

        slow = head
        fast = head.next
        
        # find middle and end listnode
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next # start of second half (before reverse)
        slow.next = None # first half end points to None
        prev = None

        # reverse second portion of list
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        # merge two halfs
        # 1>2>3>None    first
        # None<4<5<6    second
        first, second = head, prev 

        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2


        # 0 -> 1 -> 2 -> 4
        # 6 -> 5 -> 4 -> None
        # until the pointer meets


        