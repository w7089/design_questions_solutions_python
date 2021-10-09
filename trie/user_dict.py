class Node(UserDict):
    is_complete_word = False
    
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = Node()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        trie = self.trie
        for c in word:
            if c in trie:
                trie = trie[c]
            else:
                trie[c] = Node()
                trie = trie[c]
        trie.is_complete_word = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        trie = self.trie
        for c in word:
            if c not in trie:
                return False
            trie = trie[c]
        return trie.is_complete_word

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        trie = self.trie
        for c in prefix:
            if c not in trie:
                return False
            trie = trie[c]
        return True
