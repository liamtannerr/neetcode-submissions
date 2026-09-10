class TrieNode:

    def __init__(self, val: str=""):
        self.val = val
        self.children = {}
        self.word_end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for i, c in enumerate(word):
            if c not in cur.children:
                new_node = TrieNode(c)
                cur.children[c] = new_node
            cur = cur.children[c]
            if i == len(word) - 1:
                cur.word_end = True

    def search(self, word: str) -> bool:
        if not self.root.children:
            return False
        cur = self.root

        def dfs(cur, i):
            if i == len(word):
                return cur.word_end
            c = word[i]

            if c == ".":
                res = False
                for child in cur.children:
                    res = res or dfs(cur.children[child], i + 1)
                return res
            else:
                if c not in cur.children:
                    return False
                return dfs(cur.children[c], i + 1) 

        return dfs(cur, 0)        
