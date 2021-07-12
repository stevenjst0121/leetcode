from collections import defaultdict
from typing import List


class Solution:
    def __init__(self):
        self.ranks = {}

    def addRank(self, person: str, ranks: List[str]) -> None:
        self.ranks[person] = ranks

    def hasMutualRanking(self, char: str, rank: int) -> bool:
        other = self.ranks[char][rank]
        other_rank = -1
        for i, person in enumerate(self.ranks[other]):
            if person == char:
                other_rank = i
        return rank == other_rank

    def changePair(self, char: str, index: int) -> List[List[str]]:
        if index < 1:
            return None

        before = []
        if self.hasMutualRanking(char, index - 1):
            before.append(self.ranks[char][index - 1])
        if self.hasMutualRanking(char, index):
            before.append(self.ranks[char][index])

        self.ranks[char][index - 1], self.ranks[char][index] = (
            self.ranks[char][index],
            self.ranks[char][index - 1],
        )
        after = []
        if self.hasMutualRanking(char, index - 1):
            after.append(self.ranks[char][index - 1])
        if self.hasMutualRanking(char, index):
            after.append(self.ranks[char][index])

        return [before, after]


def test_has_mutual_ranking():
    solution = Solution()
    solution.addRank("a", ["b", "c", "d"])
    solution.addRank("b", ["a", "c", "d"])
    solution.addRank("c", ["d", "a"])
    solution.addRank("d", ["a", "c"])

    assert solution.hasMutualRanking("a", 0)
    assert solution.hasMutualRanking("a", 1)
    assert not solution.hasMutualRanking("a", 2)


def test_change_pair():
    solution = Solution()
    solution.addRank("a", ["b", "c", "d"])
    solution.addRank("b", ["a", "c", "d"])
    solution.addRank("c", ["d", "a"])
    solution.addRank("d", ["a", "c"])

    result = solution.changePair("c", 1)
    assert result == [["a"], ["d"]]
