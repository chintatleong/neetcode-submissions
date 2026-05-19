# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        start = ListNode()

        if (list1 == None):
            return list2
        
        if (list2 == None):
            return list1

        if (list1.val > list2.val):
            start = list2
        else:
            start = list1

        while list1 != None and list2 != None:
            if (list1.val > list2.val):
                temp1 = list1.next
                temp2 = list2.next

                list2.next = list1
                list2 = temp2
            else:
                temp1 = list1.next
                temp2 = list2.next

                list1.next = list2
                list1 = temp1

        return start
            