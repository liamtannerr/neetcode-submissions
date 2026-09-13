# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:   

        if not root:
            return ""

        res = []

        def dfs(cur):
            if cur:
                res.append(str(cur.val))
            else:
                res.append("n")
                return
            dfs(cur.left)
            dfs(cur.right)

        dfs(root)
        return ",".join(res)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == "":
            return None

        tree = data.split(",")
        self.i = 0

        def dfs():
            if tree[self.i] == "n":
                self.i += 1
                return None
            node = TreeNode(int(tree[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()





