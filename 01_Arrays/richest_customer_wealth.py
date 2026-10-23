class Solution(object):
    def maximumWealth(self, accounts):

        wealth = []

        for customer in accounts:
            total = sum(customer)
            wealth.append(total)

        return max(wealth)



        