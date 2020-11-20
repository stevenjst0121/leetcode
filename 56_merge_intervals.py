import pytest
from typing import *
from collections import *


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        [MEMO] Using sorted method, was thinking too complicated in implementation
        Build merged result while looping, so the last one in merged is always the one to consider merging into
        No extra space is needed

        Understand graph solution below as well
        """
        intervals.sort(key=lambda x: x[0])

        merged = []
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """Graph solution, understand but don't use as it exceeds time limit
        O(N^2) for formatting the graph
        """
        # [NOTE] To get all node in graph if graph in not connected
        graph = {tuple(interval): set() for interval in intervals}
        for i, interval_i in enumerate(intervals):
            for j, interval_j in enumerate(intervals):
                if i == j:
                    continue

                if not interval_i[1] < interval_j[0] and not interval_j[1] < interval_i[0]:
                    # they are connected
                    graph[tuple(interval_i)].add(tuple(interval_j))
                    graph[tuple(interval_j)].add(tuple(interval_i))

        # iterate through graph
        merged = []
        # [NODE] Standard DFS
        visited = set()
        for root in graph.keys():
            if root in visited:
                continue

            interval = None
            stack = [root]
            while stack:
                node = stack.pop()
                if not interval:
                    interval = list(node)
                else:
                    interval[0] = min(interval[0], node[0])
                    interval[1] = max(interval[1], node[1])
                # [NODE] Don't forget to add to visited
                visited.add(node)

                for neighbor in graph[node]:
                    if neighbor not in visited:
                        stack.append(neighbor)

            merged.append(interval)

        return merged
