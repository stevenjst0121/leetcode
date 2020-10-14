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


class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nodes = {}
        self.is_end = False

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        curr = self
        for char in word:
            if char in curr.nodes.keys():
                curr = curr.nodes[char]
            else:
                curr.nodes[char] = Trie()
                curr = curr.nodes[char]
        curr.is_end = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        curr = self
        for char in word:
            if not char in curr.nodes.keys():
                return False

            curr = curr.nodes[char]

        if not curr.is_end:
            return False

        return True

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        curr = self
        for char in prefix:
            if not char in curr.nodes.keys():
                return False

            curr = curr.nodes[char]

        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)


def test_solution():
    trie = Trie()

    assert trie.insert("apple") is None
    assert trie.search("apple")
    assert not trie.search("app")
    assert trie.startsWith("app")
    assert trie.insert("app") is None
    assert trie.search("app")
