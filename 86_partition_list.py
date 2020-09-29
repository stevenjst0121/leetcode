import pytest
from typing import *
from collections import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        dummy_head_s = ListNode()
        dummy_head_l = ListNode()
        curr = head
        curr_s = dummy_head_s
        curr_l = dummy_head_l
        while curr is not None:
            if curr.val < x:
                curr_s.next = ListNode(val=curr.val)
                curr_s = curr_s.next
            else:
                curr_l.next = ListNode(val=curr.val)
                curr_l = curr_l.next
            curr = curr.next

        # Combine
        if dummy_head_s.next is None:
            return dummy_head_l.next

        if dummy_head_l.next is None:
            return dummy_head_s.next

        curr_s.next = dummy_head_l.next
        return dummy_head_s.next
