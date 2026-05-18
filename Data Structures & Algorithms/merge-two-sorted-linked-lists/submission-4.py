# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        start = res

        if (list1 == None):
            return list2
        
        if (list2 == None):
            return list1

        
        

        while list1 != None and list2 != None:
            if (list1.val > list2.val):
                res.next = list2
                res = res.next
                list2 = list2.next
            
            else:
                res.next = list1
                res = res.next
                list1 = list1.next
        
        if list1 != None:
            res.next = list1
        
        if list2 != None:
            res.next = list2



        

        return start.next
            