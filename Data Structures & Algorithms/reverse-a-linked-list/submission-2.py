# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head

        while current:
            next_node = current.next   # save next
            current.next = prev        # reverse link
            prev = current             # move prev forward
            current = next_node        # move current forward

        return prev

"""
        if head == None:
            return None

        if head.next == None:
            return head


        post = head.next
        current = head
        prev = None

        while post.next != None:
            current.next = prev
            prev = current
            current = post
            post = post.next

        post.next = current
        current.next = prev

        return post

"""

        

