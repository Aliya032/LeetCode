# 02-07-2024 00:37
#https://www.youtube.com/watch?v=ycAq8iqh0TI
#https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii


class Solution:
    def removeDuplicates(self, nums: list[int]):
        l, r = 0, 0

        while r < len(nums):
            count = 1
            while r + 1 < len(nums) and nums[r] == nums[r + 1]:
                r += 1
                count += 1

            for i in range(min(2, count)):
                nums[l] = nums[r]
                l += 1
            r += 1

        return l
    
dupliremoved = Solution()
print(dupliremoved.removeDuplicates([1,1,1,2,2,3,3]))