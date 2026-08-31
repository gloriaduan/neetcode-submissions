class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""

        for i in range(len(s)):
            l, r = i, i
            while l > -1 and r < len(s) and s[l] == s[r]:
                res = max(res , s[l:r + 1], key = len)
                l -= 1
                r += 1
            
            l, r = i, i + 1
            while l > -1 and r < len(s) and s[l] == s[r]:
                res = max(res, s[l: r + 1], key = len)
                l -= 1
                r += 1
        
        return res
