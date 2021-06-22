# Replication of C++ atoi function
# Replication of C++ Atoi function
class Solution:
    def myAtoi(self, s: str) -> int:
        # Read in and ignore any leading whitespace
        s = s.strip()
        if s == "" or s == "-": return 0
        
        
        intString = ""
        
        # Check if next character is - or +
        numberIdx = 0
        if s[0] == "-" or s[0] == "+":
            if s[0] == "-":
                intString += "-"
            numberIdx = 1
        
        while numberIdx < len(s) and s[numberIdx].isnumeric():
            intString += s[numberIdx]
            numberIdx += 1
        
        if intString == "" or intString == "-": return 0
        convertedInt = int(intString)
        
        
        if convertedInt < -2 ** 31:
            return -2 ** 31
        elif convertedInt > 2 ** 31 - 1:
            return 2 ** 31 - 1
        else:
            return convertedInt
        
        
        
        
        
