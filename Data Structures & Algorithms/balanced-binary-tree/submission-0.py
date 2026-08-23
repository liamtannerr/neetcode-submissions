# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        self.isBalanced = True

        def dfs(cur):

            if not cur:
                return 0

            leftHeight = dfs(cur.left)
            rightHeight = dfs(cur.right)

            if abs(leftHeight - rightHeight) > 1:
                self.isBalanced = False

            return 1 + max(leftHeight, rightHeight)

        dfs(root)
        return self.isBalanced


        