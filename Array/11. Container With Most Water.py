class Solution(object):
    def maxArea(self, height):
        p1 = 0
        p2 = len(height)-1
        ans = 0
        while p1 < p2:
            h = min(height[p1],height[p2])
            w = p2-p1
            ans = max(ans, h*w)

            if height[p1] < height[p2]:
                p1+=1
            else:
                p2-=1
        return ans
