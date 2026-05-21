# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # if len(rest) < k, leave the nodes
        # reverse and then make A

        # Loop this 
            # reverse and then make B
            # Make A points to B (MUST)
            # entire thing become A 
        # Second loop
            # reverse and then make new B
            # Make A point B and become A (MUST)

        # dummy to track new answers
        dummy = ListNode()      

        # first check
        if not self.check_k(head, k):   # if less than k initially then just return head
            return head
            
        # initial looping to make A
        prev = None
        curr = head
        start = curr

        count = 0
        while count < k:        # reversing the first group of 3
            count += 1
            nxt = curr.next
            curr.next = prev

            prev = curr
            curr = nxt

        dummy.next = prev         # end of first group becomes the new head
        
        # now prev is 3
        while True:
            if curr and (self.check_k(curr, k)):
                count = 0
                end = curr
                prev = None

                while count < k:
                    count += 1

                    if (curr == None):
                        break
                    nxt = curr.next
                    curr.next = prev

                    prev = curr
                    curr = nxt

                B = prev
                start.next = B
                start = end
            else:
                B = curr
                start.next = B
                break
            
        return dummy.next


    def check_k(self, node, k):
        for _ in range(k):
            if not node:
                return False

            node = node.next

        return True