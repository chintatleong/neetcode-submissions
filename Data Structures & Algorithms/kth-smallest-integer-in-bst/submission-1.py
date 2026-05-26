# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []

        def dfs(node):
            nonlocal res
            if not node:
                return None

            # go to the left most first
            dfs(node.left)

            # after completely explored left, do something
            res.append(node.val)

            # go right after you explored left and done something
            dfs(node.right)
        
        dfs(root)

        return res[k-1]
