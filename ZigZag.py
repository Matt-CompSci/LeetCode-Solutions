# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        zigZag = []
        
        for row in range(0, numRows):
            zigZag.append([])
        
        goingDown = True
        curRow = 0
        
        for char in list(s):
            
            zigZag[curRow].append(char)
            
            if goingDown and curRow + 1 < numRows:
                curRow += 1
            elif curRow - 1 >= 0:
                curRow -= 1
            
            if curRow == 0: goingDown = True
            if curRow == numRows - 1: goingDown = False
        
        finalString = ""
        for row in zigZag:
            finalString += "".join(row)
        return finalString
                
            
