class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        valid = {")":"(","]":"[","}":"{"}
        for c in s:
            if c in valid.values():
                stack.append(c)
            elif c in valid.keys():
                if not stack or valid[c]!=stack.pop():
                    return False
        if stack:
            return False
        return True
