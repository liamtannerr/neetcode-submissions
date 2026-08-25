# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        
        def dfs(curr, floor, ceiling):
            if not curr:
                return True
            
            if not(floor < curr.val < ceiling):
                return False

            return dfs(curr.left, floor, curr.val) and dfs(curr.right, curr.val, ceiling)


        return dfs(root, -math.inf, math.inf)

            
        

            








