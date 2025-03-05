class Solution(object):
    def maxSubArray(self, nums):
        ans = 0
        x = nums[0]

        for i,num in enumerate(nums):
            if i == 0:
                ans = x
                continue

            if x < 0:
                x = 0
            x += num
            ans = max(ans, x)
        return ans

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