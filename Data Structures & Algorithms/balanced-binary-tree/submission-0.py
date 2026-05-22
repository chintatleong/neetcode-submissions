# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        abs_diff = 0
        
        def dfs(node):
            nonlocal abs_diff
            if (node == None):
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)

            if abs(left - right) > abs_diff:
                abs_diff = abs(left - right)

            return 1 + max(dfs(node.left),dfs(node.right))

        dfs(root)

        if (abs_diff > 1):
            return False
        else:
            return True