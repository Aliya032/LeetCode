#27-06-2024 23:33
#
#https://www.youtube.com/watch?v=RcZsTI5h0kg&t=1s

from collections import defaultdict
class Solution: 
    def groupAnagrams(self, strs: list[str]):
        anagram_app = defaultdict(list)
        result = []

        for s in strs:
            sorted_s = tuple(sorted(s))
            anagram_app[sorted_s].append(s)

        for value in anagram_app.values():
            result.append(value)

        return result

solution_new = Solution()
print(solution_new.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
