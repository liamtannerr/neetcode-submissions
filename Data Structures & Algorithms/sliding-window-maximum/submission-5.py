import math

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:


        q = collections.deque()
        res = []

        for i, num in enumerate(nums[:k]):
            while q and num > q[-1][1]:
                q.pop()
            q.append((i, num))

        res.append(q[0][1])

        for i, num in enumerate(nums[k:], start=k):
            if (i - k + 1) > q[0][0]:
                q.popleft()
            while q and num > q[-1][1]:
                q.pop()
            q.append((i, num))
            res.append(q[0][1])

        return res