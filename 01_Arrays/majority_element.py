class Solution:
    def majorityElement(self, nums):
        for num in nums:
            if nums.count(num) > len(nums) // 2:
                return num
        
        

