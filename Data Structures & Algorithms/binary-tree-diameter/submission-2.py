# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.hash_map = {}

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # longest edge between 2 nodes
        # left edge can add right edge
        # allow O(n) space

        # for each node you compute the sum of left and right max depth
        # but this resultant length can not be propagate up to be summed
        # hash, for each node, can you compute max depth for each node's l and r and you store in hash
        # you return the max

        self.traverse_node(root)

        return max(self.hash_map.values())


    def maxDepth(self, node):
        if (node == None):
            return 0

        return 1 + max(self.maxDepth(node.left), self.maxDepth(node.right))

    def cal_diameter(self, left, right):
        total = self.maxDepth(left) + self.maxDepth(right)
        
        return total
    
    def traverse_node(self, node):
        if (node == None):
            return None

        self.traverse_node(node.left)
        self.traverse_node(node.right)

        current_sum = self.cal_diameter(node.left, node.right)
        self.hash_map[node] = current_sum

        