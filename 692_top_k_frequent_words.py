from collections import defaultdict, Counter
from typing import List
import heapq


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        """Solution 2
        Use heapify, though solution says it's O(NlogK), but heapify should be O(NlogN), just like sort
        But it does prove that using heapify is faster than sort
        """
        # [NOTE] How to use Counter
        word_counts = Counter(words)
        heap = [(-1 * count, word) for word, count in word_counts.items()]
        heapq.heapify(heap)
        return [heapq.heappop(heap)[1] for _ in range(k)]

    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        """Draft 1
        Use sort, the problem here is that you need to sort by reverse count but word in asc order
        O(NlogN)
        """
        word_counts = defaultdict(int)
        for word in words:
            word_counts[word] += 1

        counts = sorted([(-1 * count, word) for word, count in word_counts.items()])
        return [word for _, word in counts[:k]]
