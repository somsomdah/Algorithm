class Solution(object):
    def twoSum(self, numbers, target):

        numDict = {}
        n = len(numbers)

        for i in range(n):
            num = numbers[i]
            if num in numDict.keys():
                numDict[num].append(i)
                continue
            numDict[num] = [i]

        for i in range(n):
            num = numbers[i]
            find = target - numbers[i]
            if find in numDict.keys():
                tmp = numDict[find]
                if find == num:
                    return [tmp[0]+1, tmp[1]+1]
                return [i+1, tmp[0]+1]
