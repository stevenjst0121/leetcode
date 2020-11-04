from typing import List


class Solution:
    class TrieNode:
        def __init__(self, val: str = None):
            """
            [MEMO] Implementation of TrieNode
            """
            self.val = val
            self.children = {}  # char -> Node
            self.isEnd = False

    def __init__(self):
        self.trie = Solution.TrieNode()
        self.visited = None

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """Draft 1
        The idea of using a trie is ok, but may be a bit overkill (use hash set is probably good enough)
        Key here is to use memoization to reduce duplicates in recursive calls
        """
        self.visited = [False] * len(s)
        for word in wordDict:
            node = self.trie
            word_len = len(word)
            for index, char in enumerate(word):
                if char in node.children:
                    node = node.children[char]
                else:
                    node.children[char] = Solution.TrieNode(char)
                    node = node.children[char]

                if index == (word_len - 1):
                    node.isEnd = True

        return self.canBreak(s, 0)

    def canBreak(self, s: str, start: int) -> bool:
        if start >= len(s):
            return True

        if self.visited[start]:
            return False

        node = self.trie
        for index, char in enumerate(s[start:]):
            if char not in node.children:
                self.visited[start] = True
                return False

            node = node.children[char]
            if node.isEnd and self.canBreak(s, start + index + 1):
                return True
        self.visited[start] = True
        return False
