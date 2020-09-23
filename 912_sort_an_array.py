"""
Given an array of integers nums, sort the array in ascending order.
"""
from typing import *
from collections import deque
import pdb
import pytest


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        """
        Selection sort
        """
        for i in range(len(nums)):
            min_pos = i
            for j in range(i + 1, len(nums)):
                if nums[j] < nums[min_pos]:
                    min_pos = j
            nums[i], nums[min_pos] = nums[min_pos], nums[i]
        return nums

    # def sortArray(self, nums: List[int]) -> List[int]:
    #     """
    #     Bubble sort
    #     """
    #     for i in range(len(nums) - 1):
    #         swapped = False
    #         for j in range(len(nums) - 1 - i):
    #             if nums[j] > nums[j + 1]:
    #                 nums[j], nums[j + 1] = nums[j + 1], nums[j]
    #                 swapped = True

    #         if not swapped:
    #             break
    #     return nums

    # def sortArray(self, nums: List[int]) -> List[int]:
    #     """
    #     Insertion sort
    #     Need to move elements while looping and then insert
    #     Get key before hand because we are modifying nums while looping
    #     """
    #     for i in range(1, len(nums)):
    #         key = nums[i]
    #         j = i - 1
    #         while key < nums[j] and j >= 0:
    #             nums[j + 1] = nums[j]
    #             j = j - 1
    #         nums[j + 1] = key

    #     return nums

    # def sortArray(self, nums: List[int]) -> List[int]:
    #     """
    #     Quick sort, do the compare and then divide
    #     """
    #     self.quick_sort_helper(nums, 0, len(nums) - 1)
    #     return nums

    # def sortArray(self, nums: List[int]) -> List[int]:
    #     """
    #     Merge sort, divide and then merge while comparing
    #     """
    #     self.merge_sort_helper(nums, 0, len(nums) - 1)
    #     return nums

    # def sortArray(self, nums: List[int]) -> List[int]:
    #     """
    #     Counting sort, sorting list of data in specific range
    #     Assuming range is 0-9
    #     """
    #     map = {x: 0 for x in range(10)}
    #     for element in nums:
    #         map[element] = map[element] + 1

    #     sum = 0
    #     for k, v in map.items():
    #         sum = sum + v
    #         map[k] = sum

    #     result = []
    #     print(map)
    #     for k, v in map.items():
    #         for _ in range(v - len(result)):
    #             result.append(k)
    #     return result

    # def sortArray(self, nums: List[int]) -> List[int]:
    #     """
    #     Bucket sort: use for list of data from uniformly distributed range, e.g. 0-1
    #     """
    #     buckets = []
    #     for _ in range(10):
    #         buckets.append(deque())

    #     for num in nums:
    #         index = int(num * 10)
    #         if len(buckets[index]) == 0:
    #             buckets[index].append(num)
    #         else:
    #             inserted = False
    #             for i, n in enumerate(buckets[index]):
    #                 if num < n:
    #                     inserted = True
    #                     buckets[index].insert(i, num)
    #                     break
    #             if not inserted:
    #                 buckets[index].append(num)

    #     result = []
    #     for i in range(10):
    #         for num in buckets[i]:
    #             result.append(num)

    #     return result

    # -----------------------------
    # Helpers
    # -----------------------------

    def quick_sort_helper(self, nums: List[int], low: int, high: int):
        if low >= high:
            return

        pi = self.partition_helper(nums, low, high)
        self.quick_sort_helper(nums, low, pi - 1)
        self.quick_sort_helper(nums, pi + 1, high)

    def partition_helper(self, nums: List[int], low: int, high: int):
        """
        Tip: While looping, make sure to skip the pivot index (in this case it's just high)
        """
        i = low
        pivot = nums[high]

        for j in range(low, high):
            if nums[j] < pivot:
                nums[i], nums[j] = nums[j], nums[i]
                i = i + 1
        nums[i], nums[high] = nums[high], nums[i]
        return i

    def merge_sort_helper(self, nums: List[int], low: int, high: int):
        # End confition
        if low >= high:
            return

        # Partition
        middle = low + int((high - low) / 2)
        self.merge_sort_helper(nums, low, middle)
        self.merge_sort_helper(nums, middle + 1, high)

        # Merge
        self.merge_helper(nums, low, high, middle)

    def merge_helper(self, nums: List[int], low: int, high: int, middle: int):
        if nums[middle] < nums[middle + 1]:
            return

        i = low
        j = middle + 1
        while i <= middle and j <= high:
            if nums[i] <= nums[j]:
                i = i + 1
            else:
                # Shift all elements between i and j
                val = nums[j]
                for k in range(j, i, -1):
                    nums[k] = nums[k - 1]
                nums[i] = val

                # All pointers need to be incremented!
                i = i + 1
                j = j + 1
                middle = middle + 1


@pytest.mark.parametrize(
    "test_input,expected",
    [([5, 2, 3, 1], [1, 2, 3, 5]), ([5, 1, 1, 2, 0, 0], [0, 0, 1, 1, 2, 5])],
)
def test_solution(test_input, expected):
    s = Solution()
    assert s.sortArray(test_input) == expected


# @pytest.mark.parametrize(
#     "test_input,expected",
#     [
#         (
#             [0.78, 0.17, 0.15, 0.18, 0.98, 0.45, 0.33, 0.34, 0.01],
#             [0.01, 0.15, 0.17, 0.18, 0.33, 0.34, 0.45, 0.78, 0.98],
#         )
#     ],
# )
# def test_solution(test_input, expected):
#     """
#     For bucket sort
#     """
#     s = Solution()
#     assert s.sortArray(test_input) == expected
