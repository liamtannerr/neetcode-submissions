class Solution:
    def isPalindrome(self, s: str) -> bool:
        lower = s.lower()
        i = 0
        j = len(s) - 1
        while i < j and i < len(s) and j >= 0:
            front = lower[i]
            back = lower[j]
            if(not front.isalnum()):
                i = i + 1
                continue
            if(not back.isalnum()):
                j = j - 1
                continue
            if(front != back):
                return False
            i = i + 1
            j = j - 1
        
        return True


        