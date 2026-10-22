class Solution(object):
    def runningSum(self, nums):

        result = []
        total = 0

        for num in nums:
            total += num
            result.append(total)

        return result







        