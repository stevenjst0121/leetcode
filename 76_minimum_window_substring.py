from collections import Counter, defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """Solution 1
        [MEMO] Moving window implementation
        Nested loops:
        1. Outer loop is for "expanding" the current window, and keep track of current condition
        2. Inner loop is for "contracting" the current window if the current window satisfies condition

        TODO - Optimized moving window
        """
        dict_t = Counter(t)
        required = len(dict_t)

        l, r = 0, 0
        formed = 0
        window_counts = defaultdict(int)

        ans = ""
        while r < len(s):
            c_r = s[r]
            window_counts[c_r] += 1
            if c_r in dict_t and window_counts[c_r] == dict_t[c_r]:
                formed += 1

            while l <= r and formed == required:
                if not ans or r - l + 1 < len(ans):
                    ans = s[l : r + 1]

                c_l = s[l]
                window_counts[c_l] -= 1
                if c_l in dict_t and window_counts[c_l] < dict_t[c_l]:
                    formed -= 1
                l += 1
            r += 1
        return ans
