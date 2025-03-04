class Trie:

    def __init__(self,is_end= False):
        self.links = {}
        self.is_end = is_end

    def insert(self, word: str) -> None:
        curr = self
        for w in word:
            if w not in curr.links:
                new_obj = Trie()
                curr.links[w] = new_obj
                curr = curr.links[w]
            else:
                curr = curr.links[w]
        curr.is_end = True

    def search(self, word: str) -> bool:
        curr = self
        for w in word:
            if w not in curr.links:
                return False
            else:
                curr = curr.links[w]
        return curr.is_end

    def startsWith(self, prefix: str) -> bool:
        curr = self
        for w in prefix:
            if w not in curr.links:
                return False
            else:
                curr = curr.links[w]
        return True