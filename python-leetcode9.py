print("Leetcode 9: Best Time to Buy and Sell Stock")

class Solution(object):
    def maxProfit(self, prices):

        profits = []

        # check if at least 2 prices to compare 
        if len(prices) < 2:
            return 0
        
        # compare the price and futur prices
        for i in range(len(prices) - 1):
            if(prices[i] == max(prices)):
                profits.append(0)
            else:
                for j in range(i+1, len(prices)):
                    # if there is a profit, store it
                    if prices[i] < prices[j]:
                        profits.append(prices[j] - prices[i])
                    else :
                        profits.append(0)

        # get the max profit        
        return max(profits)

        # this code works but that made the time limit exceeded error because of O(n2) time complexity
        
        # this is the fixed version

        # min_price = prices[0]
        # 
        # max_profit = 0
        # for price in prices[1:]:
        #     profit = price - min_price
        #     max_profit = max(max_profit, profit)
        #     min_price = min(min_price, price)
        
        # return max_profit

        # 
        # 
        # 
        # 
        # 
        #     
   
# test cases 
sol = Solution()
arr = [1,2]
result = sol.maxProfit(arr)
print(result) # should return 5

