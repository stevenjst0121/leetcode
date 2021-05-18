from typing import List
from collections import defaultdict, deque


class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        pmap = defaultdict(list)
        for i in range(len(ppid)):
            pmap[ppid[i]].append(pid[i])

        result = []
        queue = deque([kill])
        while queue:
            size = len(queue)
            for _ in range(size):
                process = queue.popleft()
                result.append(process)
                queue.extend(pmap[process])
        return result
