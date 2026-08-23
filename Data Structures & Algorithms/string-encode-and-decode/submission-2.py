class Solution:

    def encode(self, strs: List[str]) -> str:

        res = ""
        
        for s in strs:
            res = res + str(len(s)) + '#' + s
        
        return res

    def decode(self, s: str) -> List[str]:

        res = []

        i = 0

        while i < len(s):
            length = ""
            curString = ""
            while s[i] != '#':
                length = length + s[i]
                i += 1
            
            lengthInt = int(length)
            i += 1
            for j in range(lengthInt):
                curString = curString + s[i + j] 
            
            i += lengthInt
            
            res.append(curString)
        
        return res
            

