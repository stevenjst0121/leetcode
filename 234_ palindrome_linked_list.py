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
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True

        dummyHead = ListNode()
        dummyHead.next = head
        slow = fast = dummyHead
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        first = head
        second = slow.next
        slow.next = None

        # Reverse second list
        dummyHead = ListNode()
        curr = second
        while curr:
            next = curr.next
            curr.next = dummyHead.next
            dummyHead.next = curr
            curr = next
        second = dummyHead.next

        # Compare two lists
        while first and second:
            if first.val != second.val:
                return False
            first = first.next
            second = second.next

        return True

    # def isPalindrome(self, head: ListNode) -> bool:
    #     """
    #     Note 1: Check palindrome over list is easy, use two pointers
    #     Note 2: [MEMO] Recursion, this is advanced, but it's NOT O(1) space!!!
    #     Pretty much same as puting into reverse queue. But this only loops n once.
    #     Note 3: Reverse second half and then compare two lists
    #     """
    #     self.front = head
    #     return self.isParlindromeHelper(head)

    # def isParlindromeHelper(self, curr: ListNode) -> bool:
    #     if not curr:
    #         return True

    #     if not self.isParlindromeHelper(curr.next):
    #         return False
    #     if self.front.val == curr.val:
    #         self.front = self.front.next
    #         return True

    #     return False
