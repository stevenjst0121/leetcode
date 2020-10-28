from typing import List
from collections import defaultdict


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return None

        result = []

        # acquire dict of p
        d_p = defaultdict(int)
        for c in p:
            d_p[c] += 1

        # add 0 ~ j - 1 to dict
        d_s = defaultdict(int)
        for c in s[: len(p) - 1]:
            d_s[c] += 1

        i, j = 0, len(p) - 1
        while j < len(s):
            # Remove i - 1 and add j
            if i > 0:
                if d_s[s[i - 1]] == 1:
                    del d_s[s[i - 1]]
                else:
                    d_s[s[i - 1]] -= 1
            d_s[s[j]] += 1

            if d_s == d_p:
                result.append(i)

            i += 1
            j += 1

        return result
