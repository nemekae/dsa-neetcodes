# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: 
            return []
        
        res, q = [], deque(([root]))

        while q:
            res.append([node.val for node in q])
            q = deque([child for node in q for child in (node.left, node.right) if child])

        return res