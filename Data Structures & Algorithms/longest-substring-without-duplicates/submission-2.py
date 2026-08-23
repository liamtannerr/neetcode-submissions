class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        charSet = set()
        maxS = 0
        curLen = 0
        left = 0
        right = 1


        for right in range (len(s)):
            while s[right] in charSet:
                charSet.remove(s[left])
                left += 1
            
            charSet.add(s[right])
            curLen = right - left + 1
            maxS = max(curLen, maxS)

        return maxS