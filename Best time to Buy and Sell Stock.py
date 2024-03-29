class Solution(object):
    def maxProfit(self, prices):
        if len(prices) == 0:
            return 0
        min_price = prices[0]
        max_profit = 0
        for i in range(1,len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            elif prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price
        return max_profit

# Driver Code
prices = [7,1,5,3,6,4]
obj = Solution()
print(obj.maxProfit(prices))
