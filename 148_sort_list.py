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
    def sortList(self, head: ListNode) -> ListNode:
        """
        Note 1: No need to calculate length, just have one pointer move twice as faster, make sure to use a dummyHead to start with
        Note 2: This is top-down approach, which uses O(logN) space due to recursive call stack, use bottom-up approach to use O(1) space. Though time is still O(logN)
        Note 3: When merging, don't create new nodes. Existing nodes can be used directly.
        Note 4: Top-down approach uses O(logN) space due to recursion. Do bottom-up interations to use O(1) space
        """
        return self.sortListHelper(head)

    def sortListHelper(self, head: ListNode) -> ListNode:
        # stop condition
        if head is None or head.next is None:
            return head

        # partition
        head_1, head_2 = self.partition(head)

        # call self
        head_1 = self.sortListHelper(head_1)
        head_2 = self.sortListHelper(head_2)

        # merge
        newHead = self.merge(head_1, head_2)
        return newHead

    def partition(self, head: ListNode) -> Tuple:
        # Returns two heads
        dummyHead = ListNode()
        dummyHead.next = head
        curr = dummyHead
        ahead = dummyHead
        while ahead is not None and ahead.next is not None:
            curr = curr.next
            ahead = ahead.next.next

        head_2 = curr.next
        curr.next = None
        head_1 = head
        return (head_1, head_2)

    def merge(self, head_1: ListNode, head_2: ListNode) -> ListNode:
        """
        MEMO
        """
        dummyHead = ListNode()
        curr = dummyHead

        curr_1 = head_1
        curr_2 = head_2
        while curr_1 is not None and curr_2 is not None:
            if curr_1.val >= curr_2.val:
                curr.next = curr_2
                curr_2 = curr_2.next
            else:
                curr.next = curr_1
                curr_1 = curr_1.next
            curr = curr.next

        if curr_1 is not None:
            curr.next = curr_1
        if curr_2 is not None:
            curr.next = curr_2

        return dummyHead.next
