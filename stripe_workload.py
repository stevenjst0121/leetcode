# https://www.1point3acres.com/bbs/thread-276462-1-1.html
# https://www.1point3acres.com/bbs/thread-470073-1-1.html

from typing import List


class Solution:
    def __init__(self):
        self.nums_set = set()

    @classmethod
    def next_server_number(self, nums: List):
        nums_set = set(nums)
        N = len(nums_set)
        for num in range(1, N + 2):
            if num not in nums_set:
                return num

        raise RuntimeError("Something went wrong...")

    def allocate(self, name):
        N = len(self.nums_set)
        for num in range(1, N + 2):
            if num not in self.nums_set:
                self.nums_set.add(num)
                return f"{name}{num}"

    def deallocate(self, name):
        num = 0
        multiplier = 0
        for i in range(len(name) - 1, -1, -1):
            if name[i].isnumeric():
                num += 10 ** multiplier * int(name[i])
            else:
                break

        if num in self.nums_set:
            self.nums_set.remove(num)


def test_next_server_numer():
    solution = Solution()

    nums = [5, 3, 1]
    assert solution.next_server_number(nums) == 2

    nums = [5, 4, 1, 2]
    assert solution.next_server_number(nums) == 3

    nums = [3, 2, 1]
    assert solution.next_server_number(nums) == 4

    nums = [2, 3]
    assert solution.next_server_number(nums) == 1

    nums = []
    assert solution.next_server_number(nums) == 1


def test_allocate():
    solution = Solution()

    assert solution.allocate("apibox") == "apibox1"

    assert solution.allocate("apibox") == "apibox2"

    solution.deallocate("apibox1")

    assert solution.allocate("apibox") == "apibox1"