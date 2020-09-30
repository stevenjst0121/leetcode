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
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        """
        Draw the damn thing while working on it
        """
        if k == 1:
            return head

        dummyHead = ListNode()
        dummy = dummyHead
        front = end = head
        while end:
            kk = k
            prev = None
            while kk > 0 and end:
                if kk == 1:
                    prev = end
                end = end.next
                kk -= 1

            # break if not enough items for k groups
            if kk > 0:

                break

            # reverse front - end
            prev.next = None
            curr = end
            start = front
            while start:
                temp = start.next
                start.next = curr
                curr = start
                start = temp

            # continue
            dummy.next = curr
            dummy = front
            front = end

        return dummyHead.next
