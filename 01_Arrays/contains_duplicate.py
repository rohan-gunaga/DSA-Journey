class Solution(object):
    def containsDuplicate(self, nums):

        seen = set()

        for number in nums:
            if number in seen:
                return True

            else:
                seen.add(number)

        return False