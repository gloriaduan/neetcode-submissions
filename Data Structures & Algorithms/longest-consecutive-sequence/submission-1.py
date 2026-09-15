class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        nums.sort()
        m = {}

        for num in nums:
            if num not in m:
                if (num - 1) in m:
                    m[num] = m[num - 1] + 1
                else:
                    m[num] = 1
        
        return max(m.values())
