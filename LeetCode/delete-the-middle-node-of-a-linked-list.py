# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    
    def deleteMiddle(self, head):

        n = 0
        tmp = head
        
        while tmp:
            tmp = tmp.next
            n += 1
            
        if n == 1:
            return None
            
        ptr = head
        
        cnt = 0
        while ptr:
            cnt += 1
            if cnt == n//2:
                ptr.next = ptr.next.next
            ptr = ptr.next
                
        return head
