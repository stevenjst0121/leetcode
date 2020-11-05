from typing import List
from collections import deque


class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        """Draft 1
        Beats 96%
        """
        exclusives = [0] * n
        stack = deque()
        for log in logs:
            event = log.split(":")
            event[0] = int(event[0])
            event[2] = int(event[2])
            if event[1] == "start":
                if stack:
                    # previous function has executed for some time, add it
                    exclusives[stack[-1][0]] += event[2] - stack[-1][2]
                stack.append(event)
            elif event[1] == "end":
                prev = stack.pop()
                exclusives[prev[0]] += event[2] - prev[2] + 1
                if stack:
                    # previous event start again after this event
                    stack[-1][2] = event[2] + 1
        return exclusives
