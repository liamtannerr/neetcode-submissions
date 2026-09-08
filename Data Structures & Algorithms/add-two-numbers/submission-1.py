# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        cur1 = l1
        cur2 = l2
        carry_over = False
        count = 0

        while cur1 or cur2:

            if cur1 and cur2:
                cur_sum = cur1.val + cur2.val
            elif cur1:
                cur_sum = cur1.val
            else:
                cur_sum = cur2.val

            if carry_over:
                cur_sum += 1

            if cur_sum > 9:
                cur_sum = cur_sum - 10
                carry_over = True
            else:
                carry_over = False

            if count > 0:
                next_node = ListNode(cur_sum)
                cur_sum_node.next = next_node
                cur_sum_node = next_node
            else:
                dummy = ListNode()
                cur_sum_node = ListNode(cur_sum)
                dummy.next = cur_sum_node
                count += 1
            if cur1:
                cur1 = cur1.next
            if cur2:
                cur2 = cur2.next

        if carry_over:
            cur_sum_node.next = ListNode(1)

        return dummy.next

        

            
