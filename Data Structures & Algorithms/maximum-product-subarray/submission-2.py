class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prefix = 1
        suffix = 1
        prod = nums[0]

        for i in range(len(nums)):

            suffix = suffix * nums[i]
            prefix = prefix * nums[len(nums)- i - 1]
            prod = max(prod, max(suffix, prefix))

            if suffix == 0:
                suffix = 1
            if prefix == 0:
                prefix = 1

        return prod