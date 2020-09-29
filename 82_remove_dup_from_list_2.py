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
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        """
        Hint: Draw the picture!
        """
        if head is None or head.next is None:
            return head

        dummyHead = ListNode()
        dummyHead.next = head
        prev = dummyHead
        ahead = head.next

        has_dup = False
        while ahead is not None:
            if ahead.val == prev.next.val:
                has_dup = True
                ahead = ahead.next
            else:
                if has_dup:
                    prev.next = ahead
                    ahead = ahead.next
                    has_dup = False
                else:
                    prev = prev.next
                    ahead = ahead.next

        if has_dup:
            prev.next = None

        return dummyHead.next
