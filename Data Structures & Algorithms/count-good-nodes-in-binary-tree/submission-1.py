# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(cur, curMax):
            if not cur:
                return 0

            curMax = max(curMax, cur.val)

            if cur.val >= curMax:
                return 1 + dfs(cur.left, curMax) + dfs(cur.right, curMax)
            else:
                return dfs(cur.left, curMax) + dfs(cur.right, curMax)

        return dfs(root, root.val)
            
            
