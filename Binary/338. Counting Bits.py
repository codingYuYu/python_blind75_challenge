class Solution(object):
    def countBits(self, n):
        dp = [0]
        for i in range(1, n + 1):
            if i % 2 == 1:
                dp.append(dp[i - 1] + 1)
            else:
                dp.append(dp[i / 2])
        return dp

'''

Example 1:

Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10
Example 2:

Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101

'''