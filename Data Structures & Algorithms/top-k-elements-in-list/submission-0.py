class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] = freq[num] + 1
            else:
                freq[num] = 1

        ocurrences = [[] for i in range (len(nums) + 1)]

        for number in freq:
            ocurrences[freq[number]].append(number)
        
        res = []
        for count in ocurrences[::-1]:
            if len(res) >= k:
                break
            for num in count:
                if len(res) >= k:
                    break
                res.append(num)
        
        return res