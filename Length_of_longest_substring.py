# Calculate max length of substring with none repeating characters
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1: return 1
        if len(s) == 2: return s[0] != s[1] and 2 or 1
        
        charList = list(s)
        maxSubstringLength = 0
        currentSubstringLength = 0
        
        for idx, startChar in enumerate(charList):
            currentCharList = []
            currentSubstringLength = 0
            for char in charList[idx:len(charList)]:
                if char in currentCharList:
                    if currentSubstringLength > maxSubstringLength:
                        maxSubstringLength = currentSubstringLength
                        currentSubstringLength = 0
                else:
                    currentSubstringLength += 1
                    currentCharList.append(char)
        return maxSubstringLength
