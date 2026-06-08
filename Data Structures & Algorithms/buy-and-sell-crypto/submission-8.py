class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result=0
        buy=0
        sell=0
        for i in range(len(prices)):
                if prices[buy]>prices[sell]:
                        buy=sell
                result=max(result, prices[sell]-prices[buy])
                sell+=1
        return result

                
                
                
                
        