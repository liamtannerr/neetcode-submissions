# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(curr, cur_max):
            if not curr:
                return 0

            if curr.val >= cur_max:
                return 1 + dfs(curr.right, curr.val) + dfs(curr.left, curr.val)
            else:
                return dfs(curr.right, cur_max) + dfs(curr.left, cur_max)
        
        return dfs(root, -100)