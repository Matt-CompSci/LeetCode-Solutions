class Solution:
    def intToRoman(self, num: int) -> str:
        romanDict = {
            "M" : 1000,
            "CM" : 900,
            "D" : 500,
            "CD" : 400,
            "C" : 100,
            "XC" : 90,
            "L" : 50,
            "XL" : 40,
            "X" : 10,
            "IX" : 9,
            "V" : 5,
            "IV" : 4,
            "III" : 3,
            "II" : 2,
            "I" : 1
        }
        
        romanStr = ""
        for symbol, value in romanDict.items():
            while num >= value:
                romanStr += symbol
                num -= value
        return romanStr
