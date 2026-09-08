class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}
        def num_to_letter(num_str):
            # int("1") + 64 = 65 -> chr(65) is 'A'
            if int(num_str) > 26:
                return None

            return chr(int(num_str) + 64)
    
        def helper(s, pos, memo):
            if pos in memo:
                return memo[pos]

            if pos > len(s) - 1:
                return 1
            
            if s[pos] == "0":
                return 0
            if num_to_letter(s[pos]) and (pos < len(s) - 1 and num_to_letter(s[pos:pos+2])):
                memo[pos+1] = helper(s, pos+1, memo)
                memo[pos+2] = helper(s, pos+2, memo)
                return helper(s, pos+1, memo) + helper(s, pos+2, memo)
            if num_to_letter(s[pos]):
                memo[pos+1] = helper(s, pos+1, memo)
                return helper(s, pos+1, memo)

            return 0
        
        return helper(s, 0, memo)