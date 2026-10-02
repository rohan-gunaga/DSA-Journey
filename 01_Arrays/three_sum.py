class Solution(object):
    def threeSum(self, nums):

        result = set()

        for i in range(len(nums)):
            seen = set()

            for j in range(i + 1, len(nums)):
                needed = -(nums[i] + nums[j])

                if needed in seen:
                    triplet = sorted([nums[i], nums[j], needed])
                    result.add(tuple(triplet))

                seen.add(nums[j])
                
        return [list(triplet) for triplet in result]    


        
        