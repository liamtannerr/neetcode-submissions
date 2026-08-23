class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if (len(s) != len(t)):
            return False
        T = {}
        S = {}

        for i in range (len(s)):
            T[t[i]] = 1 + T.get(t[i], 0) 
            S[s[i]] = 1 + S.get(s[i], 0)

        return S == T