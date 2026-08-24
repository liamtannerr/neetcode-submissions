# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
                
        def dfs(curr, subCurr):
            if not curr and not subCurr:
                return True
            if (not curr and subCurr) or (not subCurr and curr):
                return False
            return (curr.val == subCurr.val) and dfs(curr.left, subCurr.left) and dfs(curr.right, subCurr.right)
        
        if not root:
            return False

        return dfs(root, subRoot) or (self.isSubtree(root.left, subRoot)) or (self.isSubtree(root.right, subRoot)) 