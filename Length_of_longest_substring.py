class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
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
