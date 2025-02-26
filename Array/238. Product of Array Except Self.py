class Solution(object):
    def productExceptSelf(self, nums):
        n = len(nums)
        ans = [1] * n

        # Calculate prefix products
        for i in range(1,n):
            ans[i] = ans[i-1] * nums[i-1]

        # Calculate suffix products
        presuffix = 1
        for i in range(n-2,-1,-1):
            presuffix *= nums[i+1]
            ans[i] *= presuffix

        return ans
