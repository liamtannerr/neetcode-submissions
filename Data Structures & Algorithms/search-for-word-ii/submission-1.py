class TrieNode:

    def __init__(self, val: str=""):
        self.val = val
        self.children = {}
        self.word_end = False

class TriePrefixTree:

    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word:str) -> None:
        cur = self.root
        for i, c in enumerate(word):
            if c not in cur.children:
                new_node = TrieNode(c)
                cur.children[c] = new_node
            cur = cur.children[c]
            if i == len(word) - 1:
                cur.word_end = True

    def prefix(self, node:TrieNode, char:str) -> bool:
        return char in node.children

    def search(self, node:TrieNode, char:str) -> bool:
        return char in node.children and node.children[char].word_end


class Solution:

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        tree = TriePrefixTree()
        for word in words:
            tree.insert(word)

        def invalid_path(r, c, visited, cur_row) -> bool:
            if r < 0 or c < 0 or r >= len(board) or c >= len(board[cur_row]):
                return True
            if (r, c) in visited:
                return True
            return False

        res = []

        def dfs(r, c, cur_node, cur_word, visited, cur_row):
            if invalid_path(r,c,visited,cur_row) or not tree.prefix(cur_node, board[r][c]):
                return
            cur_word += board[r][c]
            if tree.search(cur_node, board[r][c]):
                cur_words_in_search.append(cur_word)
                cur_node.children[board[r][c]].word_end = False

            
            visited.add((r, c))
            dfs(r + 1, c, cur_node.children[board[r][c]], cur_word, visited, cur_row)
            dfs(r - 1, c, cur_node.children[board[r][c]], cur_word, visited, cur_row)
            dfs(r, c + 1, cur_node.children[board[r][c]], cur_word, visited, cur_row)
            dfs(r, c - 1, cur_node.children[board[r][c]], cur_word, visited, cur_row)
            visited.remove((r, c))
            

        for row in range(len(board)):
            for col in range(len(board[row])):
                cur_words_in_search = []
                dfs(row, col, tree.root, "", set(), row)
                res.extend(cur_words_in_search)

        return res 