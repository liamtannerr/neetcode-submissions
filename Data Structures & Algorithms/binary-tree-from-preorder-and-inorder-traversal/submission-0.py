# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        self.indices = {}

        for i in range (len(inorder)):
            self.indices[inorder[i]] = i

        self.idx = 0

        def dfs(l, r):

            if (l > r):
                return None
            
            cur_val = preorder[self.idx]
            self.idx += 1
            cur = TreeNode(cur_val)
            mid = self.indices[cur_val]
            cur.left = dfs(l, mid - 1)
            cur.right = dfs(mid + 1, r)

            return cur




        return dfs(0, len(inorder) - 1)

        

        