
# faster
# time: O(n)
# space: O(1)
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        
        return True if goal == 0 else False

# slower
# time: O(n^2)
# space: O(n)
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [0] * n
        dp[0] = 1
        for i in range(n-1):
            if dp[i]==1:
                if (i+nums[i]+1)>n-1:
                    last = n
                else:
                    last = i+nums[i]+1
                for j in range(i,last):
                    dp[j] = 1
        return bool(dp[-1])