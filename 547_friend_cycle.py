from typing import List
from collections import defaultdict


class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        """Draft 1
        Basically DFS (solution 1)
        """
        graph = defaultdict(set)
        N = len(M)
        for i in range(N):
            for j in range(N):
                if M[i][j] == 1:
                    graph[i].add(j)

        visited = set()
        ans = 0
        for student, friends in graph.items():
            if student in visited:
                continue

            visited.add(student)
            friends = list(friends)
            while friends:
                friend = friends.pop()
                if friend in visited:
                    continue

                visited.add(friend)
                friends.extend([student for student in graph[friend] if student not in visited])
            ans += 1

        return ans