class Solution:
    def isPalindrome(self, s: str) -> bool:
        lower = s.lower()
        i = 0
        j = len(s) - 1
        while i < j:
            front = lower[i]
            back = lower[j]
            if(not front.isalnum()):
                i += 1
                continue
            if(not back.isalnum()):
                j -= 1
                continue
            if(front != back):
                return False
            i += 1
            j -= 1

        return True

        