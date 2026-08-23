# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(cur, minVal, maxVal):

            if not cur:
                return True

            if minVal >= cur.val or maxVal <= cur.val:
                return False

            return dfs(cur.left, minVal, cur.val) and dfs(cur.right, cur.val, maxVal)

        return dfs(root, -1000, 1000)









