# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        
        count = 0
        ptr = head
        
        while ptr:
            count += 1
            ptr = ptr.next
        
        if count == n:
            return head.next
        
        k = count - n
        ptr = head
        
        for i in range(1, count):
            if i == k:
                ptr.next = ptr.next.next
            ptr = ptr.next
        
        return head
        
            
