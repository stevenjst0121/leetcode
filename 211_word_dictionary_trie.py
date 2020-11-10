class WordDictionary:
    """Solution 1
    [MEMO MEMO] Use dict to implement trie, use "$" to indicate is end. Memorize the way to how add "$" and check "$"
    My original passed code had similar approach (with customized data structure instead of just using dict, and more code...)
    Solution is not faster than own code
    """

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        node = self.trie

        for ch in word:
            if not ch in node:
                node[ch] = {}
            node = node[ch]
        node["$"] = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any letter.
        """

        def search_in_node(word, node) -> bool:
            for i, ch in enumerate(word):
                if not ch in node:
                    # if the current character is '.'
                    # check all possible nodes at this level
                    if ch == ".":
                        for x in node:
                            if x != "$" and search_in_node(word[i + 1 :], node[x]):
                                return True
                    # if no nodes lead to answer
                    # or the current character != '.'
                    return False
                # if the character is found
                # go down to the next level in trie
                else:
                    node = node[ch]
            return "$" in node

        return search_in_node(word, self.trie)