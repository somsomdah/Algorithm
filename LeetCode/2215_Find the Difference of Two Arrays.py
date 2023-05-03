from collections import deque

class Solution(object):
    def findDifference(self, nums1, nums2):

        numset1 = deque(sorted(list(set(nums1))))
        numset2 = deque(sorted(list(set(nums2))))

        n1 = len(numset1)
        n2 = len(numset2)

        answer = [[],[]]

        n = max(n1, n2)

        while numset1 and numset2:
            num1 = numset1[0]
            num2 = numset2[0]

            if num1 < num2:
                answer[0].append(numset1.popleft())
            elif num2 < num1:
                answer[1].append(numset2.popleft())
            else:
                numset1.popleft()
                numset2.popleft()

        if numset1:
            answer[0].extend(list(numset1))
        if numset2:
            answer[1].extend(list(numset2))

        return answer
