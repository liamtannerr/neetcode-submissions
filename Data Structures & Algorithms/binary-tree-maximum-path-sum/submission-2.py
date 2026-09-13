# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        self.res = -math.inf

        def dfs(cur):
        
            if not cur:
                return 0
        
            left_max = max(dfs(cur.left), 0)
            right_max = max(dfs(cur.right), 0)
     
            self.res = max(self.res, cur.val + left_max + right_max)
            child_max = max(left_max, right_max)

            return max(cur.val + child_max, cur.val)

        dfs(root)
        return self.res

