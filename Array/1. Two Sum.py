class Solution(object):
    def twoSum(self, nums, target):
        # 初始一個dict用來存放已看過的數字
        number_map = {}
        # 遍歷list
        # 用target和當前檢視數字的差去dict中尋找是否有這個數字
        # 有的話回傳這個Pair
        for i,num in enumerate(nums):
            diff = target - num
            if diff in number_map:
                return [i, number_map[diff]]
            number_map[num] = i
        return None

'''
Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
'''