# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class NodeWrapper:
    def __init__(self):
        self.node = node

    def __lt__(self, other):
        return self.node.val < other.node.val

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # find the lowest common

        # O(h) time and O(h) space where h = log n
        
        # means we need to traverse top to bottom. Speed is logn 
        # Case 1: both p and q <= node, answer on left. 
            # if node == p or node == q -> p or q is the answer
        # Case 2: both p and q >= node, answer on right
        # Case 3: p and q are splitted, node is the LCS.
        
        if not root or not p or not q:
            return None
        if (max(p.val, q.val) < root.val):
            return self.lowestCommonAncestor(root.left, p, q)
        elif (min(p.val, q.val) > root.val):
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root
        
        

            

        