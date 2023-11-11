# 11-11-2023
# https://leetcode.com/problems/palindrome-number/description/
# https://redquark.org/leetcode/0009-palindrome-number/

class Solution: 
    def isPalindrome(self, x:int) -> bool:
        # Base condition
        if x < 0:
            return False
        
        # Store the number in a variable
        number = x

        reverse = 0
        while number:
            reverse = reverse * 10 + number % 10
            number //= 10

        return x == reverse
    
solution = Solution()
x = 121
print('Is this number',x,'a palindrome?',solution.isPalindrome(x))

y = -121
print('Is this number',y,'a palindrome?',solution.isPalindrome(y))

z = 10
print('Is this number',z,'a palindrome?',solution.isPalindrome(z))


