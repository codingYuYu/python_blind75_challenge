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
'''
Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

'''