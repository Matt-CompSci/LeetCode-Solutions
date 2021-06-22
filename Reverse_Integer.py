class Solution:
    def reverse(self, x: int) -> int:
        intStr = str(x)
        
        if intStr[0] == "-":
            reversedInt = int(intStr[1:][::-1])
            reversedInt *= -1
        else:
            reversedInt = int(intStr[::-1])
        
        minInt = -2 ** 31
        maxInt = 2 ** 31 - 1
        
        if reversedInt > maxInt: return 0
        if reversedInt < minInt: return 0
        return reversedInt
