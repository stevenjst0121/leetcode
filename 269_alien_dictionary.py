# Got to the point to construct a directed graph for all letters,
# and detect if the order is valid by checking if there is any loop
# from any of the node. But stuck at topological sort to find one possible
# anseer.

from typing import List
from collections import defaultdict, deque, Counter


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        """Solution 1 - BFS through words"""

        # Step 0: create data structures + the in_degree of each unique letter to 0.
        # [MEMO] Use an in_degree list for a reverse graph counter
        adj_list = defaultdict(set)
        in_degree = Counter({c: 0 for word in words for c in word})

        # Step 1: We need to populate adj_list and in_degree.
        # For each pair of adjacent words...
        # [MEMO] Use zip to reduce code when traversing through two lists of different length
        for word_1, word_2 in zip(words, words[1:]):
            for char_1, char_2 in zip(word_1, word_2):
                if char_1 != char_2:
                    if char_2 not in adj_list[char_1]:
                        adj_list[char_1].add(char_2)
                        in_degree[char_2] += 1
                    break
            else:
                # [MEMO] Use for...else...
                if len(word_2) < len(word_1):
                    return ""

        # Step 2: We need to repeatedly pick off nodes with an indegree of 0.
        # [MEMO] The way to use queue for traverse reverse graph
        output = []
        queue = deque([char for char in in_degree if in_degree[char] == 0])
        while queue:
            char = queue.pop()
            output.append(char)
            for neighbor in adj_list[char]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.appendleft(neighbor)

        # If not all letters are in output, that means there was a cycle and so
        # no valid ordering. Return "" as per the problem description.
        # [MEMO] When there are items left in in_degree means there is a loop
        # e.g [b <- a, c <- b, a <- c]
        if len(output) < len(in_degree):
            return ""
        # Otherwise, convert the ordering we found into a string and return it.
        return "".join(output)
