class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        cur_freq = {}
        for c in t:
            cur_freq[c] = cur_freq.get(c, 0) + 1

        min_chars = len(t)
        found_count = 0
        l, r = 0, 0
        res = None
        
        while r < len(s):
            front = s[r]
            if front in cur_freq:
                if cur_freq[front] > 0:
                    found_count += 1
                cur_freq[front] -= 1
            r += 1
            while found_count == min_chars:
                back = s[l]
                res = (l,r) if not res or (r - l) < (res[1] - res[0]) else res
                l += 1
                if back in cur_freq:
                    if cur_freq.get(back, 1) == 0:
                        found_count -= 1
                    cur_freq[back] += 1

        return "" if not res else s[res[0]:res[1]]