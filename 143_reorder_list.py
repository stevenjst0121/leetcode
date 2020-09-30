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
    def reorderList(self, head: ListNode) -> None:
        if not head or not head.next:
            return head

        dummyHead = ListNode()
        dummyHead.next = head
        slow = fast = dummyHead

        # Find pivot and break to two lists
        """MEMO"""
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        head_2 = slow.next
        slow.next = None

        # Reverse the second list
        head_2 = self.reverseList(head_2)

        # Merge two lists
        curr = head
        curr_2 = head_2
        while curr_2:
            temp = curr.next
            curr.next = curr_2
            curr_2 = curr_2.next
            curr.next.next = temp
            curr = temp

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
