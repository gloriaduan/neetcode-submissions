class Solution:
    def findMin(self, nums: List[int]) -> int:
        r = len(nums) - 1
        l = 0
        curr_min = nums[0]
        
        while l <= r:
            if nums[l] < nums[r]:
                curr_min = min(curr_min, nums[l])
                break

            mid = (l + r)//2
            curr_min = min(nums[mid], curr_min)
            if nums[mid] >= nums[l]:
                #search right
                l = mid + 1
            else:
                #search left
                r = mid - 1

        return curr_min