class Solution(object):
    def maxProduct(self, nums):
        n = len(nums)
        maxi = float('-inf')
        pre, suff = 1, 1

        for i in range(n):
            if pre == 0:
                pre = 1
            if suff == 0:
                suff = 1
            pre *= nums[i]
            suff *= nums[n - i - 1]
            maxi = max(maxi, pre, suff)

        return int(maxi)