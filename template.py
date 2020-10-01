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
    def TODO(self, height: List[int]) -> int:
        """"""
        pass


@pytest.mark.parametrize(
    "test_input,expected",
    [],
)
def test_solution(test_input, expected):
    s = Solution()
    assert s.TODO(test_input) == expected
