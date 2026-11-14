class Solution(object):
    def findDisappearedNumbers(self, nums):

        seen = set(nums)
        result = []
        n = len(nums)

        for i in range(1, n + 1):
            if i not in seen:
                result.append(i)

        return result



         

        