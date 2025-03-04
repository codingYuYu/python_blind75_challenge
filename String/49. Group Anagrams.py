class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        check = defaultdict(list)

        for i,s in enumerate(strs):
            d = [0] * 26
            for c in s:
                d[ord(c) - ord('a')] += 1
            key = tuple(d)
            check[key].append(s)

        return list(check.values())
