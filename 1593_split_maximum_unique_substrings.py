from typing import *


class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        self.max = 0
        self.backtrack(s, set())
        return self.max

    def backtrack(self, s: str, seen: Set):
        """
        [MEMO] Backtrack. Greedy cannot be used because there is no local optimal solution
        """
        if not s:
            self.max = max(self.max, len(seen))
            return

        for i in range(1, len(s) + 1):
            substr = s[:i]
            if substr in seen:
                continue

            seen.add(substr)
            self.backtrack(s[i:], seen)
            seen.remove(substr)

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