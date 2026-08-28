class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        res = [0] * len(nums)
        res[0] = nums[0]
        res[1] = nums[1]

        for i in range(len(res)):
            for j in range(i + 2, len(nums)):
                res[j] = max(res[j], res[i] + nums[j])
        
        return max(res)