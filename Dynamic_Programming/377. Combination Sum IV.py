class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] *(target+1)
        dp[0] = 1
        for i in range(target+1):
            for n in nums:
                if(i-n>=0):
                    dp[i] = dp[i]+dp[i-n]
        return dp[-1]