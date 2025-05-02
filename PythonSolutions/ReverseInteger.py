# 11-11-23
# https://leetcode.com/problems/reverse-integer/description/
# https://redquark.org/leetcode/0007-reverse-integer/

class Solution: 
    def reverse(self, x: int) -> int: 
        isNegative = False
        if x < 0:
            isNegative = True
            x = -x
        
        reversedNumber = 0

        while x:
            reversedNumber = reversedNumber * 10 + x % 10
            x //= 10

        if reversedNumber >= 2 ** 31 - 1 or reversedNumber <= -2 ** 31:
            return 0
        
        return -reversedNumber if isNegative else reversedNumber
    

solution = Solution()
x = 123
print('The reversed number of ', x, 'is: ', solution.reverse(x))
# print(solution.reverse(123))