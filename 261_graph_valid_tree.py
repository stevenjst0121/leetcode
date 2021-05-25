from typing import List
from collections import defaultdict


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """Solution 2
        [MEMO] For a graph to be a tree, it must have n - 1 edges.
        And as long as a graph has n - 1 edges and also fully connected, it must not contain
        cycle, so it must be a tree!
        """
        if len(edges) != n - 1:
            return False

        graph = defaultdict(set)
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)

        seen = set([0])
        stack = [0]
        while stack:
            node = stack.pop()
            for neighbor in graph[node]:
                if neighbor in seen:
                    continue

                seen.add(neighbor)
                stack.append(neighbor)

        return len(seen) == n

    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """Draft & Solution 1
        [MEMO] A graph is a tree iff:
            1. Graph has no cycle
            2. Graph is fully connected
        [MEMO] For an undirected graph, it's a bit tricky to check cycle:
            1. Remove dummy edge (going back) while traversing
            2. Store parent in seen
        """
        if not edges:
            if n == 1:
                return True
            return False

        graph = defaultdict(set)
        for a_i, b_i in edges:
            graph[a_i].add(b_i)
            graph[b_i].add(a_i)

        self.has_cycle = False
        root = edges[0][0]
        seen = set([root])
        self.dfs(root, graph, seen)

        if self.has_cycle or len(seen) < n:
            return False
        return True

    def dfs(self, node, graph, seen):
        for neighbor in graph[node]:
            if neighbor in seen:
                self.has_cycle = True
                return

            seen.add(neighbor)
            if node in graph[neighbor]:
                graph[neighbor].remove(node)
            self.dfs(neighbor, graph, seen)
