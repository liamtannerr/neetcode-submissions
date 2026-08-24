# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        if not root.right or not root.left:
            return root
        
        def dfs(curr, target):
            if not curr:
                return False
            
            if curr.val == target.val:
                return True

            return dfs(curr.right, target) or dfs(curr.left, target)

        if (dfs(root.right, p) and dfs(root.right, q)):
            return self.lowestCommonAncestor(root.right, p, q)
        elif (dfs(root.left, p) and dfs(root.left, q)):
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return root

