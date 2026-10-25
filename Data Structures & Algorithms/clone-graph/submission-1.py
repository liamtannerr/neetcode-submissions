"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node:
            return None

        q = collections.deque()
        q.append(node)
        nodes = {}
        visited = set()
        
        while q:
            size = len(q)
            for _ in range(size):
                cur = q.popleft()
                value = cur.val
                if value in visited:
                    continue
                visited.add(value)
                for neighbour in cur.neighbors:
                    q.append(neighbour)
                new_node = Node()
                new_node.val = value
                nodes[value] = new_node


        q = collections.deque()
        q.append(node)
        visited = set()
        
        while q:
            size = len(q)
            for _ in range(size):
                cur_old = q.popleft()
                value = cur_old.val
                cur_new = nodes[value]
                if value in visited:
                    continue
                visited.add(value)
                for neighbour in cur_old.neighbors:
                    q.append(neighbour)
                    cur_new.neighbors.append(nodes[neighbour.val])

        return nodes[node.val]
                    


        



        