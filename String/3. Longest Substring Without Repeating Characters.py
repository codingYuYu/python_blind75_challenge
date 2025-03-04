class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        max_length = 0
        check = set()

        for right in range(len(s)):
            while s[right] in check:
                check.remove(s[left])
                left+=1

            check.add(s[right])
            max_length = max(max_length, right-left+1)
        return max_length