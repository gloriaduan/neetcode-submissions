class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            
            if nums[l] <= nums[mid]: # if left sorted array
                if target >= nums[l] and target < nums[mid]: # if target is between l and mid
                    r = mid - 1
                else: # if target < nums[l] or target > nums[mid], target is not between l and mid
                    l = mid + 1 
            else: #otherwise, could be right sorted or pivot area 
                if target > nums[mid] and target <= nums[r]: # if target is between mid and r
                    l = mid + 1
                else:
                    r = mid - 1

        return -1