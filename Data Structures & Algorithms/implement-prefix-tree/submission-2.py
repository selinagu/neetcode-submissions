class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        prev = self.root
        for i in range(len(word)):
            letter = word[i]
            if letter not in prev.children:
                prev.children[letter] = TrieNode()
                
            if i == len(word) - 1:
                prev.children[letter].is_word = True

            prev = prev.children[letter]

    def search(self, word: str) -> bool:
        prev = self.root
        for letter in word:
            if letter not in prev.children:
                return False
            prev = prev.children[letter]

        return prev.is_word

    def startsWith(self, prefix: str) -> bool:
        prev = self.root
        for letter in prefix:
            if letter not in prev.children:
                return False
            prev = prev.children[letter]

        return True
        