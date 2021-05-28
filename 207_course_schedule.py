from typing import List
from collections import defaultdict, deque


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """DFS Solution
        [MEMO] Mark different type visited:
        1 - In traverse
        2 - Done traverse (node has no child or all children are visited)
        """
        graph = defaultdict(set)  # course to list of its prereqs
        for pr in prerequisites:
            graph[pr[1]].add(pr[0])

        # 1 - in traverse
        # 2 - done traverse (no child or all children are visited)
        visited = {}
        for course in range(numCourses):
            if self.hasCycle(course, graph, visited):
                return False
        return True

    def hasCycle(self, course, graph, visited):
        if course in visited:
            if visited[course] == 1:
                return True
            elif visited[course] == 2:
                return False

        visited[course] = 1
        for neighbor in graph[course]:
            if self.hasCycle(neighbor, graph, visited):
                return True

        visited[course] = 2

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """Topological search
        [MEMO] This implementation I found most straight-forward
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
