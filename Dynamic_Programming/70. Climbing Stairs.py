# Top down - TLE
def climbStairs1(self, n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    return self.climbStairs(n-1)+self.climbStairs(n-2)

# Bottom up, O(n) space
class Solution(object):
    def climbStairs(self, n):
        if n == 1:
            return 1
        stair = []
        for i in range(n+1):
            stair.append(0)
        stair[1] = 1
        stair[2] = 2
        for i in range(3,n+1):
            stair[i] = stair[i-1] + stair[i-2]
        return stair[-1]
