# 11-11-23
# https://leetcode.com/problems/count-the-digits-that-divide-a-number/description/
# https://www.geeksforgeeks.org/find-count-digit-number-divide-number/


class Solution: 
    def count_digits(self, n):
        x = n
        count = 0
        
        while x != 0:
            remainder = x % 10
            x //= 10
            
            if remainder > 0 and n % remainder == 0:
                count += 1
        
        return count
    
solution = Solution()
print('The number of digits that divides this is: ', solution.count_digits(121))

print('The number of digits that divides this is: ', solution.count_digits(1248))



