# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float('-inf')

        def dfs(node):
            nonlocal res
            if not node:
                return 0
            
            # find if including, not including or start new is best)
            left = dfs(node.left)
            right = dfs(node.right)

            best = max(node.val, node.val + left, node.val + right, node.val + left + right)

            if best > res:
                res = best

            return best


        dfs(root)
        return res
            


        