class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount +1)
        dp[0] = 0
        for i in range(amount+1):
            for c in coins:
                if i - c >= 0:
                    dp[i] = min(dp[i], dp[i-c]+1)
        return  dp[-1] if dp[-1]!= amount+1 else -1


'''
Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Example 3:

Input: coins = [1], amount = 0
Output: 0

'''