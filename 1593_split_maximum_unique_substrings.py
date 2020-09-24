from typing import *


class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        seen = set()
        # return self.helper(s, seen)
        return self.helper_2(s, 0, seen)

    def helper(self, s: str, seen: Set):
        """[MEMO]
        Questions like such that doesn't seem quite possible to find a mathematical solution but only a brute
        force kind of solution is available, but is hard to write as well, usually recursion is the solution.

        Note: We are looping over the end position of strings, so the stop needs to be len(s) + 1 in range
        Note: Also, looping through a range where start == end doesn't do anything.
        Looping through a range where start > end (size default to 1) doesn't do anything either. No error is thrown!!!
        """
        ans = 0
        print(f"{s}, {seen}")
        for i in range(1, len(s) + 1):
            candicate = s[:i]
            if candicate not in seen:
                seen.add(candicate)
                ans = max(ans, 1 + self.helper(s[i:], seen))
                seen.remove(candicate)
        return ans

    def helper_2(self, s: str, start: int, seen: set):
        """
        Same logic, reusing same string without making extra copy of substrings
        """
        ans = 0
        for i in range(start + 1, len(s) + 1):
            candidate = s[start:i]
            print(candidate)
            if candidate not in seen:
                seen.add(candidate)
                ans = max(ans, 1 + self.helper_2(s, i, seen))
                seen.remove(candidate)
        return ans


if __name__ == "__main__":
    s = Solution()
    test = "ab"
    result = s.maxUniqueSplit(test)
    print(result)