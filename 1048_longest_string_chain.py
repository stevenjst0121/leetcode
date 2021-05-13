from typing import List


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        """Bottom-up solution
        [MEMO]
        """
        words.sort(key=lambda x: len(x))
        dp = {}
        for word in words:
            if len(word) == 1 or not dp:
                dp[word] = 1
                continue

            max_length = 1
            for i in range(len(word)):
                cut_word = word[:i] + word[i + 1 :]
                if cut_word in dp:
                    length = dp[cut_word] + 1
                    if length > max_length:
                        max_length = length
            dp[word] = max_length
        return max(dp.values())

    def __init__(self):
        self.memo = {}
        self.all_words = set()

    def longestStrChain(self, words: List[str]) -> int:
        for word in words:
            self.all_words.add(word)

        longest = 0
        for word in words:
            length = self.dfs(word)
            if length > longest:
                longest = length
        return longest

    def dfs(self, word) -> int:
        """
        Conduct DFS does not always require building a tree, just use the concept
        """
        if word in self.memo:
            return self.memo[word]

        max_height = 0
        for i in range(len(word)):
            cut_word = word[:i] + word[i + 1 :]
            if cut_word in self.all_words:
                height = self.dfs(cut_word)
                if height > max_height:
                    max_height = height
        self.memo[word] = max_height + 1
        return max_height + 1
