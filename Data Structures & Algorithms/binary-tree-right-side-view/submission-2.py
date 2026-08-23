# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        q = collections.deque()
        res = []
        q.append(root)

        while q:
            levelSize = len(q)
            for i in range (levelSize):
                cur = q.popleft()
                if cur:
                    if cur.left:
                        q.append(cur.left)
                    if cur.right:
                        q.append(cur.right)
                    if i + 1 == levelSize:
                        res.append(cur.val)
        
        return res