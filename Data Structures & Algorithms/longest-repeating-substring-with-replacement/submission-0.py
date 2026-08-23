class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        count = {}

        fast, slow, res, mostFrequent  = 0, 0, k, 0


        while fast < len(s):
            count[s[fast]] = 1 + count.get(s[fast], 0)
            mostFrequent = max(mostFrequent, count[s[fast]])

            while (fast - slow) - mostFrequent >= k:
                count[s[slow]] -= 1
                slow += 1
                mostFrequent = max(count.values())
            
            res = max (res, fast - slow + 1)
            fast += 1

        return res 











        