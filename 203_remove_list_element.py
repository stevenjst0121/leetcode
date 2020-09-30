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
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummyHead = ListNode()
        dummyHead.next = head
        prev = dummyHead
        curr = head

        while curr:
            if curr.val == val:
                prev.next = curr.next
                curr = prev.next
            else:
                curr = curr.next
                prev = prev.next

        return dummyHead.next
