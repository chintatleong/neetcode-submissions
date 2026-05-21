# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # n is length of list, k is number of list
        dummy = ListNode()
        curr = dummy
        best_val = 99
        best_node = None
        best_index = None
        copy_lists = []

        for li in lists:
            copy_lists.append(li)

        
        # for 

        while True:
            best_val = float('inf')
            best_node = None
            best_index = -1
            # not_all_none = False

            for i, node in enumerate(copy_lists):
                if node == None:
                    continue

                if (best_val > node.val):
                    best_val = node.val
                    best_node = node
                    best_index = i 
                    # not_all_none = True
            
            curr.next = best_node
            curr = curr.next

            if not best_index == -1:
                copy_lists[best_index] = copy_lists[best_index].next
            else:
                break

        return dummy.next

            