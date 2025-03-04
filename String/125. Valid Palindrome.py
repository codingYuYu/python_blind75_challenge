class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(c.lower() for c in s if c.isalnum())
        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1

        return True

    # string.isalpha() returns True if all characters in the string are alphabetic and there is at least one character, False otherwise.
    # string.isalnum() returns True if all characters in the string are alphanumeric and there is at least one character, False otherwise.
    # string.isdigit() returns True if all characters in the string are digits and there is at least one character, False otherwise.
    # string.lower() returns a copy of the string with all the case-based characters converted to lowercase.
    # string.upper() returns a copy of the string with all the case-based characters converted to uppercase.
    # string.strip() returns a copy of the string with both leading and trailing characters removed.
    # string.lstrip() returns a copy of the string with leading characters removed.
    # string.rstrip() returns a copy of the string with trailing characters removed.
    # string.split() returns a list of substrings separated by the given delimiter.
    # string.join() returns a string concatenated with the elements of an iterable.
    # string.find() returns the lowest index of the substring if found, otherwise -1.
    # string.rfind() returns the highest index of the substring if found, otherwise -1.
