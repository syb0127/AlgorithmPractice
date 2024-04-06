class WordDictionary:

    def __init__(self):
        #dictionary of dictionaries where each sub-dictionary is a new "path"
        self.trie = {}

    def addWord(self, word: str) -> None:
        node = self.trie

        for w in word:
            if w not in node:
                node[w] = {}
            #go down a path
            node = node[w]
            #this marks the end of a path
        node['!'] = True
        
    def search(self, word: str) -> bool: 

        def recurseSearch(word, node):
            for i, ch in enumerate(word):
                if not ch in node:
                    # if the current character is '.'
                    # check all possible nodes at this level
                    if ch == '.':
                        for x in node:
                            if x != '!' and recurseSearch(word[i + 1:], node[x]):
                                return True
                    # if no nodes lead to answer
                    # or the current character != '.'
                    return False
                # if the character is found
                # go down to the next level in trie
                else:
                    node = node[ch]
            return '!' in node
        return recurseSearch(word, self.trie)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)