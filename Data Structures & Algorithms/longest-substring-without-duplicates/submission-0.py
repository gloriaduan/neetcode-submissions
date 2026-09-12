class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curSet = set()
        l = 0
        r = 0
        res = 0

        while r < len(s):
            if s[r] not in curSet:
                curSet.add(s[r])
                res = max(res, (r-l)+1)
                r += 1
            else:
                while s[l] != s[r]:
                    curSet.remove(s[l])
                    l += 1

                curSet.remove(s[l])
                l += 1

        return res