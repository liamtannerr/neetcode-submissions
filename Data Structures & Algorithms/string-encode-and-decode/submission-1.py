class Solution:

    def encode(self, strs: List[str]) -> str:

        res = ""

        for s in strs:
            res += str(len(s))
            res += '#'
            res += s

        return res


    def decode(self, s: str) -> List[str]:    

        res = []
        i = 0
        while i < len(s):
            num = ""
            curStr = ""
            while s[i] != '#':
                num += s[i]
                i += 1
            curLen = int(num)
            i += 1
            j = 0
            while j < curLen:
                curStr += s[i]
                i += 1
                j += 1
            res.append(curStr)

        return res
            
            



