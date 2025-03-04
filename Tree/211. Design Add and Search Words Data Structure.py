class WordDictionary:

    def __init__(self, is_end=False):
        self.links = {}
        self.is_end = is_end

    def addWord(self, word: str) -> None:
        curr = self
        for w in word:
            if w not in curr.links:
                new_obj = WordDictionary()
                curr.links[w]=new_obj
                curr = curr.links[w]
            else:
                curr = curr.links[w]
        curr.is_end = True

    def search(self, word: str) -> bool:
        def dfs(word,node):
            for index, ele in enumerate(word):
                if ele == ".":
                    for key,value in node.links.items():
                        if dfs(word[index+1:],value):
                            return True
                    return False
                else:
                    if ele not in node.links:
                        return False
                    else:
                        node = node.links[ele]
            return node.is_end
        return dfs(word,self)