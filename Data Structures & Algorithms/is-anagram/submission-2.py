class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        sChars = {}
        tChars = {}

        for i in range (len(s)):
            sChars[s[i]] = sChars.get(s[i], 0) + 1
            tChars[t[i]] = tChars.get(t[i], 0) + 1
        
        return sChars == tChars

