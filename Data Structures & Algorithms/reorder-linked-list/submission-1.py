# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        if not head or not head.next:
            return

        mid = head
        end = head.next

        while end and end.next:
            end = end.next.next
            mid = mid.next

        prev = None
        tail = mid.next
        mid.next = None
        while tail:
            nextNode = tail.next
            tail.next = prev
            prev = tail
            tail = nextNode
        
        first = head
        second = prev

        while second:
            firstNext = first.next
            secondNext = second.next
            first.next = second
            second.next = firstNext
            first = firstNext
            second = secondNext


