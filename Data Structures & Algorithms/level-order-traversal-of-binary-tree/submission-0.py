# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        tree = {}
        level = 0
        
        def dfs(node, level):
            nonlocal tree

            if not node:
                return None
            else:
                tree[level] = tree.get(level, []) + [node.val]
            
            dfs(node.left, level+1)
            dfs(node.right, level+1)

        dfs(root, level)

        res = []
        for li in tree.values():
            res.append(li)
        
        return res
        

        
