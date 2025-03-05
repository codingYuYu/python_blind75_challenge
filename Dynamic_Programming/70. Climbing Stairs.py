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

'''
Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
'''