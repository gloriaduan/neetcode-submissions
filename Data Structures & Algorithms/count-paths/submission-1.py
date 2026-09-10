class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}

        def helper(m, n, memo):
            if (m,n) in memo:
                return memo[(m,n)]
            if m == 0 or n == 0:
                return 0
            
            if m == 1 or n == 1:
                return 1
            
            memo[(m,n)] = helper(m-1, n, memo) + helper(m, n-1, memo)

            return helper(m-1, n, memo) + helper(m, n-1, memo)
        
        return helper(m, n, memo)
