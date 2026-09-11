def is_palindrome(word:str) -> bool:
    return word == word[::-1]

class Solution:

    def partition(self, s: str) -> List[List[str]]:
        
        res = []

        def dfs(i, path):
            if i >= len(s):
                res.append(path.copy())
                return

            for j in range(i, len(s)):
                sub = s[i:j+1]
                if is_palindrome(sub):
                    path.append(sub)
                    dfs(j + 1, path)
                    path.pop()
                    # dfs(j + 1, path)

        dfs(0, [])
        
        return res 