class Solution:
    def maxPalindromeAtPos(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return (right - left - 1), left + 1, right - 1
        
        
    def longestPalindrome(self, s: str) -> str:
        palindromeLeft = 0
        palindromeRight = 0
        palindromeLength = 0
        
        for idx, char in enumerate(list(s)):
            # Palindrome has a single digit center
            maxOddLength, oddLeft, oddRight = self.maxPalindromeAtPos(s, idx, idx)
            
            # Palindrome has a double digit center
            maxEvenLength, evenLeft, evenRight = self.maxPalindromeAtPos(s, idx, idx + 1)
            
            # Get left and right of biggest
            left = 0
            right = 0
            length = 0
            
            # Store left right and length of the bigger palindrome
            if maxOddLength > maxEvenLength:
                left = oddLeft
                right = oddRight
                length = maxOddLength
            else:
                left = evenLeft
                right = evenRight
                length = maxEvenLength

            # If the bigger palidnrome is bigger than previously found palidnromes then set it
            # To the max
            if length > palindromeLength:
                palindromeLeft = left
                palindromeRight = right
                palindromeLength = length

        return s[palindromeLeft:palindromeRight + 1]
