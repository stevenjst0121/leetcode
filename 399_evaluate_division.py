from typing import List
from collections import defaultdict


class Solution:
    def calcEquation(
        self, equations: List[List[str]], values: List[float], queries: List[List[str]]
    ) -> List[float]:
        """Draft 1
        Track of product while traversing via DFS
        [MEMO] Trick here is to use defaultdict(dict) for graph to mark value of a -> b
        [????] Disjoint set solution
        """
        self.graph = defaultdict(dict)
        for i in range(len(equations)):
            a_i, b_i = equations[i][0], equations[i][1]
            v_i = values[i]
            self.graph[a_i][b_i] = v_i
            self.graph[b_i][a_i] = 1 / v_i

        result = []
        for c_j, d_j in queries:
            result.append(self.execute(c_j, d_j))
        return result

    def execute(self, c_j, d_j):
        seen = set([c_j])
        return self.dfs(c_j, d_j, 1, seen)

    def dfs(self, c_j, d_j, product, seen):
        if c_j not in self.graph:
            return -1

        if c_j == d_j:
            return 1

        for nei, v_j in self.graph[c_j].items():
            if nei in seen:
                continue

            if nei == d_j:
                return product * v_j

            seen.add(nei)
            res = self.dfs(nei, d_j, product * v_j, seen)
            if res > 0:
                return res
            seen.remove(nei)

        return -1