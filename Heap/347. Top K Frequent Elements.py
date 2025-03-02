class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        top_k_keys = [key for key, value in c.most_common(k)]
        return top_k_keys
