# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        dq = collections.deque() 
        dq.append(root)
        res = []

        while dq:
            current_level = []
            level_size = len(dq)
            for i in range(level_size):
                curr = dq.popleft()
                if curr:
                    dq.append(curr.left)
                    dq.append(curr.right)
                    current_level.append(curr.val)
            if current_level:
                res.append(current_level)

        return res







