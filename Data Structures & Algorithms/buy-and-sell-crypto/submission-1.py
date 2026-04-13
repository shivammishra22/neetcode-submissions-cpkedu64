class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        nums=100
        res=0
        for r in range(len(prices)):
            if(prices[r]<nums):
                nums=prices[r]
            res=max(res,(prices[r]-nums))
        return res
        