import heapq
from collections import defaultdict
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """Solution
        [DEMO] Think differently, count the number of idles needed instead
        """
        frequencies = [0] * 26
        for task in tasks:
            frequencies[ord(task) - ord("A")] += 1
        frequencies.sort()

        f_max = frequencies.pop()
        idles = (f_max - 1) * n
        while frequencies and idles > 0:
            idles -= min(f_max - 1, frequencies.pop())
        return max(0, idles) + len(tasks)

    # def leastInterval(self, tasks: List[str], n: int) -> int:
    #     """Draft 1
    #     Using min heap, T - O(N), S - O(N)
    #     The idea is just to minimize the idles needed, always start with the task that has most count first
    #     """
    #     if n == 0:
    #         return len(tasks)

    #     d = defaultdict(int)
    #     heap = []
    #     for task in tasks:
    #         d[task] += 1

    #     for task, count in d.items():
    #         # So that the the task has most count lives at top of heap
    #         heapq.heappush(heap, (-1 * count, task))

    #     # run tasks
    #     runs = 0
    #     while heap:
    #         k = 0
    #         current = []
    #         while heap and k < n + 1:
    #             current.append(heapq.heappop(heap))
    #             k += 1

    #         for count, task in current:
    #             count += 1
    #             if count != 0:
    #                 heapq.heappush(heap, (count, task))

    #         if not heap:
    #             runs += k
    #         else:
    #             runs += n + 1

    #     return runs
