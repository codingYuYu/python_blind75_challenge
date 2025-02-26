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
