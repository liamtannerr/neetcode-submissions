# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        self.tree = collections.deque()
        def dfs(curr): 
            if not curr:
                return
            if curr.left:
                dfs(curr.left)

            self.tree.append(curr.val)
               
            if curr.right:
                dfs(curr.right)
        
        dfs(root)
        return self.tree[k - 1]

