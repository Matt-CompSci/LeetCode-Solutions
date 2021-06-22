class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0): return False
        
        stringInt = str(x)
        left = 0
        right = 0
        
        # Odd number -> singular center
        center = (len(stringInt) // 2)

        if len(stringInt) % 2 == 1:
            left = center
            right = center
        # Even number -> two numbers in center
        else:
            left = center - 1
            right = center
            
        
        if stringInt[left] != stringInt[right]: return False
        
        while left > 0 and right < len(stringInt):
            left -= 1
            right += 1
            if stringInt[left] != stringInt[right]: return False
        return True
            
            
