# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        rootVal = root.val
        pVal = p.val
        qVal = q.val

        if (pVal <= rootVal and qVal >= rootVal) or (qVal <= rootVal and pVal >= rootVal):
            return root
        
        if pVal < rootVal:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return self.lowestCommonAncestor(root.right, p, q)
        