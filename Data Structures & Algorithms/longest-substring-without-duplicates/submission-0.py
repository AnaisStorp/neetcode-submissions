class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlenght = 0
        left, right = 0, 0
        last_seen = {}
        while right < len(s):
            char = s[right]
            if char in last_seen:
                left = max(left, last_seen[char]+ 1)
            last_seen[char] = right
            maxlenght = max(maxlenght, right - left +1)
            right += 1
        return maxlenght
