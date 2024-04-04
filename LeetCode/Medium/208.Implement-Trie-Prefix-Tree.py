class TrieNode:
    def __init__(self, char = ""):
        #node value itself
        self.char = char
        #recursive한 process이기 때문에 나와 내 밑에 있는 자손들을 dictionary에 보관한다
        self.children = {}
        self.is_end = False


class Trie:
    #We can save a lot of space if we use a trie instead of a hash table. 

    def __init__(self):
        #initialize data structure
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char in node.children:
                #있으면 한 칸 내려가기만 하면 됨
                node = node.children[char]
            else:
                #없으면 새로운 node를 만들기
                new_node = TrieNode(char)
                node.children[char] = new_node
                node = new_node
        #맨 밑까지 갔다는 거니까 is_end 바꿔주기
        node.is_end = True

    def search(self, word: str) -> bool:
        node = self.root
        print(node)
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)