import pytest
from typing import *
from collections import *


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def generate_list(list: List) -> ListNode:
    dummyHead = ListNode()
    curr = dummyHead
    for val in list:
        curr.next = ListNode(val)
        curr = curr.next
    return dummyHead.next


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        [MEMO] Using sorted method, was thinking too complicated in implementation
        Build merged result while looping, so the last one in merged is always the one to consider merging into
        No extra space is needed
        """
        intervals.sort(key=lambda x: x[0])

        merged = []
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged

    # def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    # """
    # [MEMO] Brute force solution, time limit exceeded. But need to understand who an undirected graph can be used
    # Graph can be implemented just using a dictionary from current graph key -> list of connected graph nodes
    # """
    #     graph = self.build_graph(intervals)
    #     node_lists = self.get_connected_nodes(graph, intervals)

    #     merged = []
    #     for nodes in node_lists:
    #         start = min(node[0] for node in nodes)
    #         end = max(node[1] for node in nodes)
    #         merged.append([start, end])
    #     return merged

    # def get_connected_nodes(self, graph, intervals):
    #     node_lists = []
    #     visited = set()

    #     for interval in intervals:
    #         if tuple(interval) not in visited:
    #             nodes = []
    #             stack = [interval]
    #             while stack:
    #                 node = stack.pop()
    #                 if tuple(node) not in visited:
    #                     nodes.append(node)
    #                     visited.add(tuple(node))
    #                     stack.extend(graph[tuple(node)])
    #             node_lists.append(nodes)

    #     return node_lists

    # def has_overlap(self, i_a, i_b):
    #     return not (i_a[0] > i_b[1] or i_b[0] > i_a[1])

    # def build_graph(self, intervals):
    #     graph = defaultdict(list)
    #     for i in range(len(intervals)):
    #         for j in range(i + 1, len(intervals)):
    #             if self.has_overlap(intervals[i], intervals[j]):
    #                 graph[tuple(intervals[i])].append(intervals[j])
    #                 graph[tuple(intervals[j])].append(intervals[i])
    #     return graph


@pytest.mark.parametrize(
    "test_input,expected",
    [],
)
def test_solution(test_input, expected):
    s = Solution()
