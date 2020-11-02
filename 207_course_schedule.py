from typing import List
from collections import defaultdict, deque


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """[MEMO] Topological search
        This implementation I found most straight-forward
        Can also define a Node object with a variable that tracks the degree of the node (See solution)
        """
        graph = defaultdict(set)
        degrees = [0] * numCourses
        for first, second in prerequisites:
            graph[first].add(second)
            degrees[second] += 1

        queue = deque([course for course, count in enumerate(degrees) if count == 0])
        while queue:
            node = queue.pop()
            for child in graph[node]:
                degrees[child] -= 1
                if degrees[child] == 0:
                    queue.appendleft(child)

        if not all([degree == 0 for degree in degrees]):
            return False
        return True

    # def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    #     graph = defaultdict(set)
    #     for first, second in prerequisites:
    #         graph[first].add(second)

    #     visited = set()
    #     checked = set()
    #     for curr in range(numCourses):
    #         if self.isCyclic(curr, graph, visited, checked):
    #             return False
    #     return True

    def isCyclic(self, curr, graph, visited, checked) -> bool:
        # [MEMO] The way to check if there is loop in graph (keep visited and erase after done for current node)
        # [MEMO] Can be improved with memoization since node can be visited multiple times
        if curr in visited:
            return True

        if curr in checked:
            return False

        visited.add(curr)

        ret = False
        for child in graph[curr]:
            ret = self.isCyclic(child, graph, visited, checked)
            if ret:
                break

        visited.remove(curr)
        if not ret:
            checked.add(curr)
        return ret
