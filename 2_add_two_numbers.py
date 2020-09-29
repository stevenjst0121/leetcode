import pytest
from typing import *
from collections import *


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """"""
        head = ListNode()
        curr = head
        carry = 0
        while l1 is not None or l2 is not None or carry > 0:
            sum = (l1.val if l1 is not None else 0) + (l2.val if l2 is not None else 0) + carry
            residule = sum % 10
            carry = int(sum / 10)
            curr.next = ListNode(val=residule)

            # increment
            curr = curr.next
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next

        return head.next
