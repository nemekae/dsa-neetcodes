"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        clones = {}  # old node -> new cloned node
        
        def dfs(curr):
            if curr in clones:
                return clones[curr]
            
            # Create clone
            clone = Node(curr.val, [])
            clones[curr] = clone
            
            # Clone neighbors
            for neighbor in curr.neighbors:
                clone.neighbors.append(dfs(neighbor))
            
            return clone
        
        return dfs(node)

