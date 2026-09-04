class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        def helper(s, wordDict, memo):
            if s in memo:
                return memo[s]

            if s == "":
                return True

            for word in wordDict:
                if s[:len(word)] == word:
                    if helper(s[len(word):], wordDict, memo):
                        memo[s[len(word):]] = True
                        return True

            memo[s] = False
            return False
            
        return helper(s, wordDict, memo)