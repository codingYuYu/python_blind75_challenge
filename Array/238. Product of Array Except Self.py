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

'''
Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

'''