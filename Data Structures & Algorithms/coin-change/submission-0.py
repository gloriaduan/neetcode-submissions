class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
            
        res = [0] * (amount + 1)

        for i in range(len(res)):
            if i == 0 or res[i] != 0:
                for num in coins:
                    if i + num < len(res):
                        if res[i + num] == 0:
                            res[i + num] = res[i] + 1
                        else:
                            res[i + num] = min(res[i + num], res[i] + 1)
        
        if res[amount] == 0:
            return -1

        return res[amount]