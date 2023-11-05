class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None: 
        # last index nums1
        last = n + m - 1

        # merge in reverse order
        while m > 0 and n > 0: 
            if nums1[m-1] > nums2[n-1]:
                nums1[last] = nums1[m - 1]
                m -= 1
            else: 
                nums1[last] = nums2[n - 1]
                n-= 1
            last -= 1

        # fill nums1 with leftover nums2 elements
        while n > 0:
            nums1[last] = nums2[n - 1]
            n, last = n-1, last-1
        print(nums1)

solution = Solution()
solution.merge([1], 1, [], 0)
solution.merge([0], 0, [1], 1)
solution.merge([1,2,3,0,0,0], 3, [2,5,6], 3)