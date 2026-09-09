class TrieNode:

    def __init__(self, val: str=""):
        self.val = val
        self.word_end = False
        self.children = {}


class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:

        cur = self.root

        for i, c in enumerate(word):
            if c not in cur.children:
                new_node = TrieNode(c)
                cur.children[c] = new_node

            cur = cur.children[c]
            if i == len(word) - 1:
                cur.word_end = True

    def search(self, word: str) -> bool:

        cur = self.root

        for i, c in enumerate(word):
            if c not in cur.children:
                return False

            if i == len(word) - 1:
                last_node = cur.children[c]
                return last_node.word_end
            cur = cur.children[c]
            
        return True
        

    def startsWith(self, prefix: str) -> bool:

        cur = self.root

        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]

        return True
        
        