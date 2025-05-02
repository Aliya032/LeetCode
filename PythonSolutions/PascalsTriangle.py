# 13-11-2023
# https://walkccc.me/LeetCode/problems/0118/
# https://leetcode.com/problems/pascals-triangle/description/
# https://takeuforward.org/data-structure/program-to-generate-pascals-triangle/

from typing import * 

def generateRow(row):
    ans = 1
    ansRow = [1] # inserting the 1st element
    
    for col in range(1, row):
        ans = ans * (row - col)
        ans = ans // col 
        ansRow.append(ans)
        
    return ansRow

class Solution:     
    def pascalTriangle(self, n: int) -> [list[list[int]]]:
        ans = []
        # store the entire pascal's triangle
        for row in range(1, n+1):
            ans.append(generateRow(row))
            
        return ans

solution = Solution()
print(solution.pascalTriangle(5))
