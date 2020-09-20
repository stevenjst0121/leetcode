"""
"""


class Solution:
    # def maximumSwap(self, num: int) -> int:
    #     """Brute force
    #     Maximum num is 10^8, so there are only 8C2 = 28 ways to swap, easy to brute force
    #     """
    #     nums = list(str(num))
    #     ans = nums[:]
    #     for i in range(len(nums)):
    #         for j in range(i + 1, len(nums)):
    #             nums[i], nums[j] = nums[j], nums[i]
    #             if nums > ans:
    #                 ans = nums[:]
    #             nums[i], nums[j] = nums[j], nums[i]
    #     return int("".join(ans))

    def maximumSwap(self, num: int) -> int:
        """Greedy
        For each number, get the last position available
        Loop through nums, find the biggest possible value in the future and swap them
        """
        nums = list(str(num))
        last = {int(n): i for i, n in enumerate(nums)}
        for i, x in enumerate(nums):
            for n in range(9, int(x), -1):
                if last.get(n, -1) > i:
                    nums[i], nums[last[n]] = nums[last[n]], nums[i]
                    return int("".join(nums))
        return num


if __name__ == "__main__":
    s = Solution()
    print(s.maximumSwap(1234))
    print(s.maximumSwap(2314))
    print(s.maximumSwap(1))
    print(s.maximumSwap(4321))
