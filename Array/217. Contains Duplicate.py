class Solution(object):
    def containsDuplicate(self, nums):
        counter = Counter(nums)
        for key, value in counter.items():
            if value > 1:
                return True
        return False


'''
Example 1:

Input: nums = [1,2,3,1]

Output: true

Explanation:

The element 1 occurs at the indices 0 and 3.

Example 2:

Input: nums = [1,2,3,4]

Output: false

Explanation:

All elements are distinct.

Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]

Output: true

'''