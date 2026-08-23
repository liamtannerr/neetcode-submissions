class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word in map:
                map[sorted_word].append(word)
            else:
                map[sorted_word] = [word]

        sol = []
        for val in map.values():
            sol.append(val)

        return sol


        


        