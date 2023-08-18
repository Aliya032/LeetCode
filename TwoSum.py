# https://leetcode.com/problems/two-sum/
# Fri 18 Aug 2023
# Question 1

class solution:
    def TwoSum(self, nums, target):
        nums_dict = {}
        for i in range(len(nums)):
            if target - nums[i] in nums_dict:
                print('the nums_dict is: ',nums_dict)
                return [nums_dict[target - nums[i]], i]
            nums_dict[nums[i]] = i


# example input:
nums = [2, 11, 15, 7]
target = 9

nums2 = [12,3,4,6,12] 
target2 = 24

#creating an instance of the solution class
sol = solution()

# calling the TwoSum method with the given input and target
result = sol.TwoSum(nums,target)
result2 = sol.TwoSum(nums2,target2)

print(result)
print(result2)