"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copy_map = {None:None}
        start = dummy = head

        while head:
            copy_map[head] = Node(head.val, None, None)
            head = head.next

        
        while dummy:
            copy_map[dummy].next = copy_map[dummy.next]
            copy_map[dummy].random = copy_map[dummy.random]
            dummy = dummy.next

        return copy_map[start]

