from typing import List
from collections import deque


class Solution:
    def isBipartite(self, graph):
        """Solution
        [MEMO+1] Use coloring to tag each node, this is faster because it avoids search upon validation
        """
        color = {}
        for node in range(len(graph)):
            if node not in color:
                stack = [node]
                color[node] = 0
                while stack:
                    node = stack.pop()
                    for nei in graph[node]:
                        if nei not in color:
                            stack.append(nei)
                            color[nei] = color[node] ^ 1
                        elif color[nei] == color[node]:
                            return False
        return True

    def isBipartite(self, graph: List[List[int]]) -> bool:
        """Draft 1
        BFS through the graph while putting different levels in to two sets
        Need to have an outer loop since the graph is guaranteed to be connected.
        Only beats 8%
        """
        if not graph:
            return False

        A = set()
        B = set()
        put_A = True
        queue = deque()
        while len(A) + len(B) < len(graph):
            for i in range(len(graph)):
                if i not in A and i not in B:
                    queue.append(i)
                    break

            while queue:
                size = len(queue)
                for _ in range(size):
                    node = queue.popleft()

                    if put_A:
                        A.add(node)
                        for neighbor in graph[node]:
                            if neighbor in A:
                                return False
                            elif neighbor not in B:
                                queue.append(neighbor)
                    else:
                        B.add(node)
                        for neighbor in graph[node]:
                            if neighbor in B:
                                return False
                            elif neighbor not in A:
                                queue.append(neighbor)

                put_A = not put_A
        return True
