import pytest
from typing import *
from collections import *


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def generate_list(list: List) -> ListNode:
    dummyHead = ListNode()
    curr = dummyHead
    for val in list:
        curr.next = ListNode(val)
        curr = curr.next
    return dummyHead.next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        """
        Note 1: Check palindrome over list is easy, use two pointers
        Note 2: [MEMO] Recursion
        Note 3: Reverse second half and then compare two lists
        """
        self.front = head
        return self.isParlindromeHelper(head)

    def isParlindromeHelper(self, curr: ListNode) -> bool:
        if not curr:
            return True

        if not self.isParlindromeHelper(curr.next):
            return False
        if self.front.val == curr.val:
            self.front = self.front.next
            return True

        return False
