from typing import List


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        """Draft 1
        Using stack, one trick here is that all items in stack must be in desc order
        """
        N = len(T)
        stack = []
        result = [0] * N

        for i, t in enumerate(T):
            while stack:
                if stack[-1][1] < t:
                    last = stack.pop()
                    result[last[0]] = i - last[0]
                    continue

                break

            stack.append((i, t))
        return result
