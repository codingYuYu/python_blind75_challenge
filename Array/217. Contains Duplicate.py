class Solution(object):
    def containsDuplicate(self, nums):
        counter = Counter(nums)
        for key, value in counter.items():
            if value > 1:
                return True
        return False