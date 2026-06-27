class PrefixTree:

    def __init__(self):
        self.prefix = []

    def insert(self, word: str) -> None:
        self.prefix.append(word)

    def search(self, word: str) -> bool:
        return word in self.prefix

    def startsWith(self, prefix: str) -> bool:
        for word in self.prefix:
            if word.startswith(prefix):
                return True

        return False
        