from collections import defaultdict
from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        """Solution 2
        [MEMO] Use Disjoint Set/Union Find
        """
        reps = [i for i in range(n)]
        components = n
        for node1, node2 in edges:
            if self.union(reps, node1, node2):
                components -= 1
        return components

    def find(self, reps, node):
        if node == reps[node]:
            return node

        rep = self.find(reps, reps[node])
        reps[node] = rep
        return rep

    def union(self, reps, node1, node2):
        rep1 = self.find(reps, node1)
        rep2 = self.find(reps, node2)

        if rep1 == rep2:
            return False

        reps[rep2] = rep1
        return True

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        """Draft 1
        Build graph and traverse
        """
        graph = defaultdict(set)
        for a_i, b_i in edges:
            graph[a_i].add(b_i)
            graph[b_i].add(a_i)

        visited = set()
        count = 0
        for node in graph.keys():
            if node in visited:
                continue

            visited.add(node)
            stack = [node]
            while stack:
                node = stack.pop()
                for neighbor in graph[node]:
                    if neighbor in visited:
                        continue

                    visited.add(neighbor)
                    stack.append(neighbor)

            count += 1
        return count + n - len(visited)
