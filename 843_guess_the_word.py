from typing import List
from random import randint


# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:


class Solution:
    def findSecretWord(self, wordlist: List[str], master: "Master") -> None:
        """Youtube solution
        [MEMO] Was initially trying to create dict mapping up front
        The key here is to reduce wordlist while trying
        """
        while wordlist:
            word = wordlist[randint(0, len(wordlist) - 1)]
            res = master.guess(word)
            if res == 6:
                break

            new_wordlist = []
            for word2 in wordlist:
                if self.countMatches(word, word2) == res:
                    new_wordlist.append(word2)
            wordlist = new_wordlist

    def countMatches(self, word1, word2):
        count = 0
        for c1, c2 in zip(word1, word2):
            if c1 == c2:
                count += 1
        return count
