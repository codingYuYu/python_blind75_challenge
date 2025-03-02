class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True  # Base case: empty string can be segmented
        
        for i in range(1, len(s) + 1):
            for j in range(0, i): 
                if dp[j] and s[j:i] in words:
                    dp[i] = True
                    break  # Stop early if we find a valid segmentation
        
        return dp[-1]
        