# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(node, left_bound, right_bound):
            if not node:
                return True

            # bound check
            if not (left_bound < node.val < right_bound):
                return False
                
            is_left = dfs(node.left, left_bound, node.val)
            is_right = dfs(node.right, node.val, right_bound)

            return is_left and is_right


        return dfs(root, float('-inf'), float('inf'))

            