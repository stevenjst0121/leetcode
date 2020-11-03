from collections import defaultdict, deque
from typing import List


class Solution:

    WHITE = 1
    GRAY = 2
    BLACK = 3

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """DFS Solution
        [MEMO] DFS from every node, and keep track of status of each node
        The idea is basically a node can be put at last if either it has no children
        or all of its children are already visited
        """
        adj_list = defaultdict(set)
        for a, b in prerequisites:
            adj_list[b].add(a)

        color = {k: Solution.WHITE for k in range(numCourses)}

        output = []
        has_cycle = False

        def dfs(node):
            # [MEMO] Important, if local function need to reassign local variable
            nonlocal has_cycle

            if color[node] == Solution.GRAY:
                # Being visied, cycle!
                has_cycle = True
                return

            if color[node] == Solution.BLACK:
                # Already visited, do nothing
                return

            color[node] = Solution.GRAY
            for neighbor in adj_list[node]:
                dfs(neighbor)

            output.append(node)
            color[node] = Solution.BLACK

        for course in range(numCourses):
            dfs(course)

        if has_cycle:
            return []

        # Seems like reverse a list is faster than using a queue to keep pushing in order
        return output[::-1]

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(set)
        degrees = [0] * numCourses

        for first, second in prerequisites:
            if first not in graph[second]:
                graph[second].add(first)
                degrees[first] += 1

        output = []
        queue = deque([course for course, num_deps in enumerate(degrees) if num_deps == 0])
        while queue:
            course = queue.pop()
            output.append(course)
            for neighbor in graph[course]:
                degrees[neighbor] -= 1
                if degrees[neighbor] == 0:
                    queue.appendleft(neighbor)

        if len(output) < numCourses:
            return []
        return output