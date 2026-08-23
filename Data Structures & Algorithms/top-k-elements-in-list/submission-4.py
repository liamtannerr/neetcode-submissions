class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        bucket = [[] for i in range(len(nums) + 1)]

        for key in freq:
            bucket[freq[key]].append(key)

        res = []

        for frequency_set in reversed(bucket):
            for num in frequency_set:
                res.append(num)
                if len(res) >= k:
                    return res

        return res

        