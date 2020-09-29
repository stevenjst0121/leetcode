import pytest
from typing import *
from collections import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummyHead = ListNode()
        dummyHead.next = head
        curr = dummyHead
        curr_n = curr  # n nodes ahead of curr
        while n > 0:
            curr_n = curr_n.next
            n -= 1

        while curr_n.next is not None:
            curr = curr.next
            curr_n = curr_n.next

        curr.next = curr.next.next
        return dummyHead.next
