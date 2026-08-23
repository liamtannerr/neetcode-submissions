class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = {}
        topK = [[] for i in range (len(nums) + 1)]
        res = []

        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        
        for num in freq:
            topK[freq[num]].append(num)


        for arr in topK[::-1]:
            for num in arr:
                res.append(num)
                if len(res) == k:
                    return res
                
        return res