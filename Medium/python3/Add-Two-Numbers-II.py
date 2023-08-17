# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        stack1, stack2 = [], []
        while l1:
            stack1.append(l1.val)
            l1=l1.next
        while l2:
            stack2.append(l2.val)
            l2=l2.next
        prev = None
        carr = 0
        while stack1 or stack2 or carr:
            summ = carr
            if stack1: summ += stack1.pop()
            if stack2: summ += stack2.pop()

            node = ListNode(summ%10)
            node.next=prev
            prev=node
            carr = summ // 10
        return prev
