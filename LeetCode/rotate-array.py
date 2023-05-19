class Solution(object):
    def rotate(self, nums, k):
        n = len(nums)
        k = k % n
        tmp = nums[-k:]+ nums[:-k]
        for i in range(n):
            nums[i] = tmp[i]
