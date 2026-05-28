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
                left_res = False 
                right_res = False

                # if left child and right child exist, we check
                if node.left and node.left.val < node.val:
                    left_res = dfs(node.left)

                if node.right and node.right.val > node.val:
                    right_res = dfs(node.right)

                # if left or right child is a None, return True
                if not node.left:
                    left_res = True

                if not node.right:
                    right_res = True
                
                
                return left_res and right_res

        return dfs(root)


                
