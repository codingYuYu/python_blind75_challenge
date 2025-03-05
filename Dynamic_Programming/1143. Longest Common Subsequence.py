class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [0] * len(text1)
        longest = 0

        for c in text2:
            cur_length = 0
            for i, val in enumerate(dp):
                if cur_length < val:
                    cur_length = val
                elif c == text1[i]:
                    dp[i] = cur_length + 1
                    longest = max(longest, cur_length + 1)

        return longest

'''
Example 1:

Input: text1 = "abcde", text2 = "ace"
Output: 3
Explanation: The longest common subsequence is "ace" and its length is 3.
Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
Example 3:

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.
'''