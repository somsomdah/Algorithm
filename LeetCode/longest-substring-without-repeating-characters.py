from collections import deque
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        alphaDict = {}

        letters = [str(c) for c in s]
        n = len(s)
        st, ed = 0, -1 # 시작 인덱스, 끝 인덱스
        res = 0
        for i in range(n):
            c = letters[i]

            if c not in alphaDict.keys():
                alphaDict[c] = -1

            idx = alphaDict[c] # 알파벳의 인덱스
            alphaDict[c] = i # 마지막으로 사용된 인덱스 저장

            if idx < st: # 사용된적이 없음
                ed = i
            else:
                if res < ed - st + 1:
                    res = ed - st + 1
                st = idx + 1
                ed = idx + 1
            print(i, st, ed)
        if res < ed - st + 1:
            res = ed - st + 1   
        return res
