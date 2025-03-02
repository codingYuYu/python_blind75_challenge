# binary search
class Solution(object):
    def findMin(self, nums):
        low = 0
        high = len(nums)-1
        while(low < high):
            mid = low + (high - low) / 2
            if(nums[mid]<nums[high]):
                high = mid
            else:
                low = mid + 1
        return nums[low]