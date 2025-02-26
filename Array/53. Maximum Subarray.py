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