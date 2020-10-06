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
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0

        L = len(beginWord)
        all_combo_dict = defaultdict(list)
        for word in wordList:
            for i in range(L):
                temp = word[:i] + "*" + word[i + 1 :]
                all_combo_dict[temp].append(word)

        return self.helper(beginWord, 0, all_combo_dict)

    def helper(self, word: str, depth: int, all_combo_dict: Dict[str, List[str]]) -> int:
        # TODO
        min = sys.maxsize
        for i in range(len(word)):
            temp = word[:i] + "*" + word[i + 1 :]
            if not all_combo_dict.get(temp, None):
                for new in all_combo_dict[temp]:
                    all_combo_dict[temp].remove(new)
                    res = self.helper(new, depth + 1, all_combo_dict)
                    if res > 0 and (depth + res) < min:
                        min = depth + res
                    all_combo_dict[temp].append(new)

        return min if min < sys.maxsize else 0
