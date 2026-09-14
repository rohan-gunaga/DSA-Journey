class Solution(object):
    def maxProfit(self, prices):
        
        minimum_price = prices[0]
        best_profit = 0

        for price in prices:
            if price < minimum_price:
                minimum_price = price


            else:
                profit = price -  minimum_price

                if profit > best_profit:
                    best_profit = profit

        return best_profit
