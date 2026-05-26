# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        counter = 0

        def dfs(node):
            nonlocal counter
            if not node:
                return None

            # go to the left most first
            left = dfs(node.left)
            if left:
                return left

            # after completely explored left, do something
            counter += 1

            if counter == k:
                return node.val

            # go right after you explored left and done something
            right = dfs(node.right)
            if right:
                return right
        
        res = dfs(root)

        return res
