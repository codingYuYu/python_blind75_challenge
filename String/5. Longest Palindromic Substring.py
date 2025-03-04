class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ""
        ans_len = 0

        for c in range(len(s)):
            l,r = c,c
            while l>=0 and r<len(s) and s[l]==s[r]:
                if (r-l+1) > ans_len:
                    ans = s[l:r+1]
                    ans_len = len(ans)
                l-=1
                r+=1
            l,r = c,c+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                if (r-l+1) > ans_len:
                    ans = s[l:r+1]
                    ans_len = len(ans)
                l-=1
                r+=1
        return ans
