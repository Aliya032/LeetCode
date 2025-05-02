# 13-06-2024 18:28 
# video solution: https://www.youtube.com/watch?v=Pcd1ii9P9ZI
# Question: https://leetcode.com/problems/remove-element/submissions/1287055386/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k

solution = Solution()
print(solution.removeElement([0.1,2,2,3,0,4,2],2))