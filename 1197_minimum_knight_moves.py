from collections import deque


class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        """
        [MEMO] Though this is not tree or graph problem, we need to use BFS here since
        we are looking for minimum moves
        In order to improve performance, use bi-directional search will save more than half the work
        Remember the implementation:
            1. Define a bfs function that takes (queue, visited, visited_other)
            2. bfs goes one level and returns True or False
            3. **** Make sure to add node to visited as soon as it's added to queue for faster search
            4. In main, call bfs from both sides
        """
        if x == 0 and y == 0:
            return 0

        visited_f = set([(0, 0)])  # (x, y)
        visited_b = set([(x, y)])  # (x, y)
        queue_f = deque([(0, 0)])
        queue_b = deque([(x, y)])
        steps_f = 0
        steps_b = 0
        while queue_f or queue_b:
            if self.bfs(queue_f, visited_f, visited_b):
                return steps_f + steps_b
            steps_f += 1

            if self.bfs(queue_b, visited_b, visited_f):
                return steps_f + steps_b
            steps_b += 1

    def bfs(self, queue, visited, visited_other) -> bool:
        offsets = [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]
        length = len(queue)
        for _ in range(length):
            pos = queue.popleft()
            if pos in visited_other:
                return True

            for offset in offsets:
                new_pos = (pos[0] + offset[0], pos[1] + offset[1])
                if new_pos not in visited:
                    queue.append(new_pos)
                    visited.add(new_pos)

        return False
