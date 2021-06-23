class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0: return ""
        
        idx = 0
        prefix = ""
        
        while True:
            if idx >= len(strs[0]): return prefix
            currentChar = strs[0][idx]
            for string in strs:
                if idx > len(string) - 1:
                    return prefix
                if string[idx] != currentChar:
                    return prefix
            idx += 1
            prefix += currentChar
            
