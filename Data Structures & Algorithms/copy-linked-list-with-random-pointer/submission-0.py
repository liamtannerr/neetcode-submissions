"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        if not head:
            return None

        og_to_copy = {}
        og_cur = head
        copy_cur = Node(og_cur.val)

        while og_cur.next:
            copy_next = Node(og_cur.next.val)
            copy_cur.next = copy_next
            og_to_copy[og_cur] = copy_cur
            copy_cur = copy_cur.next
            og_cur = og_cur.next
            
        og_to_copy[og_cur] = copy_cur

        og_cur = head
        copy_cur = og_to_copy[og_cur]

        while og_cur:
            og_random = og_cur.random
            if og_random:
                copy_cur.random = og_to_copy[og_random]
            copy_cur = copy_cur.next
            og_cur = og_cur.next

        return og_to_copy[head]