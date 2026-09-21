class Solution(object):
    def sortColors(self, nums):

        left = 0
        mid = 0
        right = len(nums) - 1

        while mid <= right:

            if nums[mid] == 0:

                nums[left], nums[right] = nums[mid], nums[left]
                left += 1
                mid += 1

            elif nums[mid] == 1:
                mid += 1

            else:
                nums[mid], nums[right] = nums[right], nums[mid]
                right -= 1










        



