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

    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        """
        This approach seems more clear to me, and it's pretty much the same as making a ring approach
        """
        if head is None or head.next is None:
            return head

        # Find length of list
        curr = head
        len = 1
        while curr.next is not None:
            len += 1
            curr = curr.next

        # calculate actual shifts needed
        kk = k % len
        if kk == 0:
            return head

        # Get curr and head
        steps_ahead = len - kk
        ahead = head
        while steps_ahead > 1:
            # Get to the node 1 step before
            ahead = ahead.next
            steps_ahead -= 1

        # Disconnect at ahead
        temp = ahead.next
        ahead.next = None
        ahead = temp

        # Connect end to head
        end = ahead
        while end.next is not None:
            end = end.next
        end.next = head

        # return new head
        return ahead
