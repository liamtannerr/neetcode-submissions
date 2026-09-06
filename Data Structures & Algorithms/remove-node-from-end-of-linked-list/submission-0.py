# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        dummy = ListNode()
        dummy.next = head

        count = 0
        cur = head

        while cur: 
            cur = cur.next
            count += 1

        cur = dummy
        for _ in range(count - n):
            cur = cur.next
        
        cur.next = cur.next.next

        return dummy.next





