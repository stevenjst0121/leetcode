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
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return head

        dummyHead = ListNode()
        dummyHead.next = head
        curr = head

        while curr.next:
            node = curr.next
            curr.next = node.next
            node.next = dummyHead.next
            dummyHead.next = node

        return dummyHead.next
