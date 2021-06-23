class Solution:
    def romanToInt(self, s: str) -> int:
        # IV
        romanDictionary = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }
        
        totalInt = 0
        
        for idx, char in enumerate(list(s)):
            totalInt += romanDictionary[char] or 0
            if idx > 0 and romanDictionary[char] > romanDictionary[s[idx - 1]]:
                totalInt -= romanDictionary[s[idx - 1]] * 2
        return totalInt
