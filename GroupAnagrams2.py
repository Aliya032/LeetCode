# https://www.youtube.com/watch?v=vzdNOK2oB2E

from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: list[str]):
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for c in s:
                   count[ord(c) - ord("a")] += 1

            res[tuple(count)].append(s)

        return res.values()
    
solution_new = Solution()
print(solution_new.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))