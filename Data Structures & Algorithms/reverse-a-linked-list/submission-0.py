# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head == None:
            return None


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



        

