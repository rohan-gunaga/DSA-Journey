class Solution(object):
    def maxSubArray(self, nums):
        
        current_sum = nums[0]
        best_sum = nums[0]

        for number in nums[1:]:
            series = current_sum + number
            fresh = number

            if series > number:
                current_sum = series
            else:
                current_sum = number

            if current_sum > best_sum:
                best_sum = current_sum

        return best_sum
            
            
