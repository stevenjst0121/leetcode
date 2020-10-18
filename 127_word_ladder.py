import sys
import pytest
from typing import *
from collections import *


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def generate_list(list: List) -> ListNode:
    dummyHead = ListNode()
    curr = dummyHead
    for val in list:
        curr.next = ListNode(val)
        curr = curr.next
    return dummyHead.next


class Solution:
    def __init__(self):
        self.word_len = 0
        self.all_combo_dict = defaultdict(list)

    def visitWordNode(
        self,
        queue: Deque[str],
        visited: Dict[str, int],
        visited_other: Dict[str, int],
    ) -> int:
        # queue should not be empty
        curr_word, level = queue.popleft()
        for i in range(self.word_len):
            trans = curr_word[:i] + "*" + curr_word[i + 1 :]
            for new_word in self.all_combo_dict[trans]:
                if new_word in visited_other.keys():
                    # word has been visited from the other side
                    return level + visited_other[new_word]

                if new_word not in visited.keys():
                    # Try the new word
                    queue.append((new_word, level + 1))
                    visited[new_word] = level + 1

        # Not found yet
        return 0

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        [MEMO] bi-directional search
        Here we don't have a tree at first, we kind of build the tree while traversing through it
        See the BFS approcah below for a queue based solution
        To optimize the BFS approach, we use bi-directional search, basically start traversing
        from both side, and keep track of visited as well as the visited level from both side.
        When visiting new node from one side, check if this node has been visited from the other side as well

        This helps to reduce search where the tree breadth is large.
        """
        if endWord not in wordList or not wordList:
            return 0

        # Add all words to dict with trans
        self.word_len = len(beginWord)
        for word in wordList:
            for i in range(self.word_len):
                trans = word[:i] + "*" + word[i + 1 :]
                self.all_combo_dict[trans].append(word)

        # Queue for iterating
        queue_front = deque([(beginWord, 1)])
        queue_back = deque([(endWord, 1)])

        # Visited
        visited_front = {beginWord: 1}
        visited_back = {endWord: 1}

        while queue_front and queue_back:
            steps = self.visitWordNode(queue_front, visited_front, visited_back)
            if steps > 0:
                return steps

            steps = self.visitWordNode(queue_back, visited_back, visited_front)
            if steps > 0:
                return steps

        return 0

    # def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
    #     """
    #     [MEMO] BFS Approach using queue
    #     Using a queue helps to reduce search (search level by level, and we can remove
    #     the level from allcombos completely after a level is added to queue)
    #     """
    #     if endWord not in wordList or not wordList:
    #         return 0

    #     # Add all words to dict with trans
    #     word_len = len(beginWord)
    #     all_combo_dict = defaultdict(list)
    #     for word in wordList:
    #         for i in range(word_len):
    #             trans = word[:i] + "*" + word[i + 1 :]
    #             all_combo_dict[trans].append(word)

    #     # Queue for iterating
    #     queue = deque()
    #     queue.append((beginWord, 1))

    #     # Visited
    #     visited = {beginWord}

    #     while queue:
    #         curr_word, level = queue.popleft()
    #         for i in range(word_len):
    #             trans = curr_word[:i] + "*" + curr_word[i + 1 :]
    #             for new_word in all_combo_dict[trans]:
    #                 if new_word == endWord:
    #                     # Found it
    #                     return level + 1

    #                 if new_word in visited:
    #                     continue

    #                 queue.append((new_word, level + 1))
    #             all_combo_dict[trans] = []  # IMPORTANT: remove words to reduce search
    #             # The recursive approach exceeded time limit because it works one-by-one
    #             # but this approcah works level-by-level

    #     # Not found
    #     return 0

    # def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
    #     if endWord not in wordList or not endWord or not beginWord or not wordList:
    #         return 0

    #     L = len(beginWord)
    #     all_combo_dict = defaultdict(list)
    #     for word in wordList:
    #         for i in range(L):
    #             temp = word[:i] + "*" + word[i + 1 :]
    #             all_combo_dict[temp].append(word)
    #     visited = set()
    #     visited.add(beginWord)
    #     steps = self.helper(beginWord, endWord, all_combo_dict, visited)
    #     return steps + 1 if steps > 0 else 0

    # def helper(
    #     self, beginWord: str, endWord: str, all_combo_dict: Dict[str, List[str]], visited: Set[str]
    # ) -> int:
    #     """
    #     Brute force, exceeds time limit
    #     """
    #     min_steps = sys.maxsize
    #     for i in range(len(beginWord)):
    #         transword = beginWord[:i] + "*" + beginWord[i + 1 :]
    #         if all_combo_dict.get(transword, None):
    #             for new in all_combo_dict[transword]:
    #                 if new == beginWord or new in visited:
    #                     continue

    #                 if new == endWord:
    #                     # Found end word
    #                     return 1

    #                 # Try the word
    #                 visited.add(new)
    #                 res = self.helper(new, endWord, all_combo_dict, visited)
    #                 if res > 0 and (res + 1) < min_steps:
    #                     min_steps = res + 1

    #                 # Done try
    #                 visited.remove(new)

    #     return min_steps if min_steps < sys.maxsize else 0


@pytest.mark.parametrize(
    "test_input,expected",
    [
        (("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]), 5),
        (("hot", "dog", ["hot", "dog"]), 0),
    ],
)
def test_solution(test_input, expected):
    s = Solution()
    assert s.ladderLength(test_input[0], test_input[1], test_input[2]) == expected
