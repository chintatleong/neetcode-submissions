# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node):
            if not node:
                return True
            else:
                if (node.left) and node.left.val >= node.val:
                    return False
                elif node.right and node.right.val <= node.val:
                    return False
                elif not node.left and not node.right:
                    return True
                
                if node.left and node.left.val < node.val:
                    return dfs(node.left)
                if node.right and node.right.val > node.val:
                    return dfs(node.right)
                
                return True

        return dfs(root)


                
