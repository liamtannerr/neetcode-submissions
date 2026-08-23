# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        self.count = 0

        def dfs(cur, curMax):
            if not cur:
                return None
            if cur.val >= curMax:
                self.count += 1

            curMax = max(curMax, cur.val)

            left = dfs(cur.left, curMax)
            right = dfs(cur.right, curMax)
            
            return None

        dfs(root, root.val)
        return self.count
            
            
