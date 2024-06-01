# 01-06-2024 23:57 
#https://leetcode.com/problems/reverse-bits/
#https://walkccc.me/LeetCode/problems/190/#__tabbed_1_3

class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0

        for i in range(32):
            if n >> i & 1:
                ans |= 1 << 31 - i
        return ans
        

solutionN = Solution()
print(solutionN.reverseBits(43261596)) # expected output: 964176192 
print(solutionN.reverseBits(4294967293)) # expected output 2: 3221225471
