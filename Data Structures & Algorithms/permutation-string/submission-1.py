class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        s1Chars, s2Chars = [0] * 26, [0] * 26

        for i in range(len(s1)):
            s1Chars[ord(s1[i]) - ord('a')] += 1
            s2Chars[ord(s2[i]) - ord('a')] += 1

        matches = 0

        for i in range(26):
            if s1Chars[i] == s2Chars[i]:
                matches += 1


        l = 0

        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            indexRight = ord(s2[r]) - ord('a')
            s2Chars[indexRight] += 1
            if s2Chars[indexRight] == s1Chars[indexRight]:
                matches += 1
            elif s2Chars[indexRight] - 1 == s1Chars[indexRight]:
                matches -= 1

            indexLeft = ord(s2[l]) - ord('a')
            s2Chars[indexLeft] -= 1
            if s2Chars[indexLeft] == s1Chars[indexLeft]:
                matches += 1
            elif s2Chars[indexLeft] + 1 == s1Chars[indexLeft]:
                matches -= 1
            l += 1

        return matches == 26


        