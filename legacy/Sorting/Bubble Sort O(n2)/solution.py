from typing import *


class Solution:
    def bubble_sort(self, arr: List):
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if arr[i] > arr[j]:
                    arr[i], arr[j] = arr[j], arr[i]

    def bubble_sort_recursive(self, arr: List, start: int):
        if start == len(arr) - 1:
            return

        for i in range(start, len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]

        self.bubble_sort_recursive(arr, start + 1)


if __name__ == "__main__":
    s = Solution()
    l = [
        4,
        2,
        1,
        5,
    ]
    # s.bubble_sort(l)
    s.bubble_sort_recursive(l, 0)
    print(l)
