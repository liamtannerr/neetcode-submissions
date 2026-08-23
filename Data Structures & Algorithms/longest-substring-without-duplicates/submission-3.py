class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        chars = set()

        fast = 0;
        slow = 0;
        Max = 0

        for fast in range(len(s)):
            while s[fast] in chars:
                chars.remove(s[slow])
                slow += 1
            
            chars.add(s[fast])
            Max = max(Max, fast - slow + 1)
       

        return Max
        