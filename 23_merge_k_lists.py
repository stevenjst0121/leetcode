import pdb
import pytest
import heapq
from queue import PriorityQueue
from typing import *
from collections import *

"""
MEMO: Python objects are passed by reference, but reference is NOT POINTER

For example,
GIVEN
    to_add = lists[i]

WHEN
    to_add = to_add.next

THAT
    lists[i] is NOT changed!!!

NEED
    lists[i] = to_add.next
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __lt__(self, other) -> bool:
        return self.val < other.val

    def __le__(self, other) -> bool:
        return self.val <= other.val


def generate_list(list: List) -> ListNode:
    dummyHead = ListNode()
    curr = dummyHead
    for val in list:
        curr.next = ListNode(val)
        curr = curr.next
    return dummyHead.next


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        """
        Optimized with priority queue, which takes O(logN) for insert and O(1) to access highest priority
        MEMO: Use of priority queue, or use heapq.heappush, heapq.heappop directly
        Note: requires definition of __lt__ (<) and __le__ (<=) in ListNode class
        """
        dummyHead = ListNode()
        curr = dummyHead
        q = PriorityQueue()
        for node in lists:
            if node is not None:
                q.put((node.val, node))

        while not q.empty():
            val, node = q.get()
            curr.next = ListNode(val=val)
            curr = curr.next
            if node.next:
                q.put((node.next.val, node.next))

        return dummyHead.next

    # def mergeKLists(self, lists: List[ListNode]) -> ListNode:
    #     """
    #     Brute force - time limit exceeded, O(KN) - Takes O(K) for adding each element to result
    #     Optimize with PriorityQueue
    #     """
    #     dummyHead = ListNode()
    #     curr = dummyHead

    #     while True:
    #         next_node_index = None
    #         for i, node in enumerate(lists):
    #             if node is None:
    #                 continue

    #             if next_node_index is None or node.val < lists[next_node_index].val:
    #                 next_node_index = i

    #         if next_node_index is None:
    #             # Done!
    #             break

    #         # Add and continue
    #         next_node = lists[next_node_index]
    #         curr.next = ListNode(val=next_node.val)
    #         curr = curr.next
    #         lists[next_node_index] = next_node.next

    #     return dummyHead.next


@pytest.mark.parametrize(
    "test_input,expected",
    [
        (
            [generate_list([1, 4, 5]), generate_list([1, 3, 4]), generate_list([2, 6])],
            generate_list([1, 1, 2, 3, 4, 4, 5, 6]),
        )
    ],
)
def test_solution(test_input, expected):
    s = Solution()
    assert s.mergeKLists(test_input) == expected


if __name__ == "__main__":
    s = Solution()
    res = s.mergeKLists([generate_list([1, 4, 5]), generate_list([1, 3, 4]), generate_list([2, 6])])
