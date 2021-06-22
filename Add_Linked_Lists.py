# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. 
# Add the two numbers and return the sum as a linked list.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        p = l1
        q = l2
        dummyHead = ListNode(0)
        curNode = dummyHead
        while p != None or q != None:
            sum = (p and p.val or 0) + (q and q.val or 0) + carry
            carry = sum // 10
            curNode.next = ListNode(sum % 10)
            curNode = curNode.next
            if p: p = p.next
            if q: q = q.next
        
        if carry > 0:
            curNode.next = ListNode(carry)
        return dummyHead.next
        
            
            
