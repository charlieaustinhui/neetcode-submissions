class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result=0
        for i,n in enumerate(prices):
                sell=0
                buy=n
                for j in range(i+1,len(prices)):
                        sell=max(prices[j],sell)
                        if (sell-buy)>result:
                                result=sell-buy
        return result

                
                
                
                
        