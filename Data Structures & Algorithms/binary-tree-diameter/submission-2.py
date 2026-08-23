# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        self.res = 0

        def dfs(cur):

            if not cur:
                return 0

            leftHeight = dfs(cur.left)
            rightHeight = dfs(cur.right)

            self.res = max(self.res, leftHeight + rightHeight)

            return 1 + max(leftHeight, rightHeight)

        dfs(root)

        return self.res