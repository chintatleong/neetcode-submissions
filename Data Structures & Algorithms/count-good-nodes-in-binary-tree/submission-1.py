# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # from root to target x
        # x is good if its the maximum along that path
        res = []
        max_val = float('-inf')

        def dfs(node, max_val):
            nonlocal res
            if not node:
                return None

            else: 
                if (node.val >= max_val):
                    res.append(node.val)
                    max_val = node.val

                dfs(node.left, max_val)
                dfs(node.right, max_val)

        dfs(root, max_val)

        return len(res)

            

