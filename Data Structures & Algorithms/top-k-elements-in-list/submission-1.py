class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        buckets = [None] * (len(nums) + 1)
        
        for num in nums:
            if num not in map:
                map[num] = 1
            else:
                map[num] += 1
        
        for key, value in map.items():
            if buckets[value] is None:
                buckets[value] = [key]
            else:
                buckets[value].append(key)
        
        i = len(buckets) - 1
        res = []
        j = 0

        while j < k and i > 0:
            if buckets[i] is not None:
                res = res + buckets[i]
                j += len(buckets[i])
            i -=1
        
        return res