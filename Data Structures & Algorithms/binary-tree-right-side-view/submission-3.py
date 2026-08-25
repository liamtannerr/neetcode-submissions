# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        dq = collections.deque()
        dq.append(root)
        res = []

        while dq:
            level_size = len(dq)
            print(f"level size: {level_size}")
            for i in range(level_size):
                curr = dq.popleft()
                
                if curr:
                    print(curr.val)
                    if curr.left:
                        dq.append(curr.left)
                    if curr.right:
                        dq.append(curr.right)
                    if i == (level_size - 1):
                        res.append(curr.val)
            print("###################")

        return res