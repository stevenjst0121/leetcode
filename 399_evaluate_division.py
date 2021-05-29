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
        graph = defaultdict(dict)
        for equation, value in zip(equations, values):
            graph[equation[0]][equation[1]] = value
            graph[equation[1]][equation[0]] = 1 / value

        results = []
        for query in queries:
            visited = set([query[0]])
            result = self.runquery(graph, query[0], query[1], visited)
            results.append(result)
        return results

    def runquery(self, graph, node, target, visited):
        # Returns value of node / target
        if node not in graph:
            return -1

        if node == target:
            return 1

        if target in graph[node]:
            return graph[node][target]

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                ret = self.runquery(graph, neighbor, target, visited)
                if ret > 0:
                    return graph[node][neighbor] * ret
        return -1
