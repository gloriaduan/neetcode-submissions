class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, path, cur_sum):
            if i > len(nums)-1 or cur_sum > target:
                return

            if cur_sum == target:
                res.append(path[:])
                return

            path.append(nums[i])
            dfs(i, path, cur_sum + nums[i])
            path.pop()
            dfs(i+1, path, cur_sum)

        dfs(0, [], 0)

        return res