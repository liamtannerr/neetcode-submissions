class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groups = defaultdict(list)
        res = []
        for word in strs:
            letters = [0] * 26
            for char in word:
                letters[ord(char) - ord('a')] += 1
            groups[tuple(letters)].append(word)
    
        res = []
        for val in groups.values():
            res.append(val)

        return res

            

                