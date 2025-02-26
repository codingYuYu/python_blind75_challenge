# Time complexity: O(log(n))
# Space complexity: O(1)
class Solution(object):
    def search(self, nums, target):
        i = 0
        j = len(nums) - 1
        while i <= j:
            mid = i + (j - i) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[i]:
                if target >= nums[i] and target < nums[mid]:
                    j = mid - 1
                else:
                    i = mid + 1
            elif nums[mid] <= nums[j]:
                if target > nums[mid] and target <= nums[j]:
                    i = mid + 1
                else:
                    j = mid - 1
        return -1


# another solution
class Solution(object):
     def search(self, nums, target):
        try:
            index = nums.index(target)
        except:
            index = -1
        return index
