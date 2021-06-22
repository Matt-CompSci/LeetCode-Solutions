# Calculate max length of substring with none repeating characters
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}
        substring_start = 0
        max_substring_len = 0
        
        for idx, char in enumerate(s):
            if char in char_map.keys():
                if char_map[char] >= substring_start:
                    substring_start = char_map[char] + 1
            max_substring_len = max(max_substring_len, idx - substring_start + 1)
            char_map[char] = idx
        return max_substring_len
