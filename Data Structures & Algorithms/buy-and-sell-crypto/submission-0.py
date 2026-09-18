class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        res = 0

        for r in range(1, len(prices)):
            if prices[r] < prices[left]:
                left = r
            else:
                res = max(res, prices[r] - prices[left])

        return res