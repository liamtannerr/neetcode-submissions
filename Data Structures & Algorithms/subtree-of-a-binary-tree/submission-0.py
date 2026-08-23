# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   

    def isSameTree(self, q: Optional[TreeNode], p: Optional[TreeNode]) -> bool:

        if (p and not q) or (q and not p):
            return False

        if not p and not q:
            return True

        return p.val == q.val and self.isSameTree(q.left, p.left) and self.isSameTree(q.right, p.right)

        
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if self.isSameTree(root, subRoot):
            return True

        if not root:
            return False
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)