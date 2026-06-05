# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        # all the left becomes right
        # all the right becomes left
        # until left is None or right is None
        if (root == None):
            return root

        self.invert(root)

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
    
    def invert(self, node):
        if (node == None):
            return None

        tmp = node.left
        node.left = node.right
        node.right = tmp 

        return node