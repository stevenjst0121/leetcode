from collections import defaultdict
import heapq


class Solution(object):
    """Was not able to figure out a solution..."""

    def reorganizeString(self, S):
        """Solution 1
        [MEMO] Brilliant solution using sort
        """
        N = len(S)
        A = []
        for c, x in sorted((S.count(x), x) for x in set(S)):
            if c > (N + 1) / 2:
                # [NOTE] This is the condition to tell if not possible
                return ""
            A.extend(c * x)
        ans = [None] * N
        # inter-insert last part and first part of the sorted chars
        ans[::2], ans[1::2] = A[N // 2 :], A[: N // 2]
        return "".join(ans)

    def reorganizeString(self, S):
        """Solution 2
        [MEMO] Smart way of using heap to pop top 2 items off
        """
        N = len(S)
        chars = defaultdict(int)
        for char in S:
            chars[char] += 1
            if chars[char] > (N + 1) / 2:
                return ""

        heap = []
        for char, count in chars.items():
            heapq.heappush(heap, (-1 * count, char))

        res = []
        while len(heap) > 1:
            first = heapq.heappop(heap)
            second = heapq.heappop(heap)
            res.append(first[1])
            res.append(second[1])
            if first[0] < -1:
                heapq.heappush(heap, (first[0] + 1, first[1]))
            if second[0] < -1:
                heapq.heappush(heap, (second[0] + 1, second[1]))
        if heap:
            res.extend(heap[0][1] * (-1 * heap[0][0]))
        return "".join(res)