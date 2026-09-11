class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}

        for s in strs:
            arr = [0] * 26

            for c in s:
                arr[ord(c) - ord("a")] += 1
            
            if tuple(arr) not in res:
                res[tuple(arr)] = [s]
            else:
                res[tuple(arr)].append(s)
        
        return list(res.values())