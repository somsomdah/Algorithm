from collections import deque

class Solution(object):
    def removeStars(self, s):
        stack = list()
        
        for ch in s:
            if ch == "*":
                stack.pop()
            else:
                stack.append(ch)
                
        return "".join(stack)
