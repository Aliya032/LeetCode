## https://leetcode.com/problems/reverse-vowels-of-a-string/description/
## 3rd November, 2023 9:38 a.m.
class Solution: 
    def reverseVowels(self, s: str) -> str:
        chars = list(s)
        vowels = {'a','e','i','o','u','A','E','I','O','U'}
        l = 0
        r = len(s)-1
        
        while l < r:
            while l < r and chars[l] not in vowels:
                l += 1
            while l < r and chars[r] not in vowels:
                r -=1
            chars[l], chars[r] = chars[r], chars[l]
            l += 1
            r -= 1
        return ''.join(chars)
    
solution = Solution()
print(solution.reverseVowels('hello'))
print(solution.reverseVowels('leetcode'))