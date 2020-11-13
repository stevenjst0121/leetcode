from typing import List


class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        if not S:
            return None

        lasts = {char: i for i, char in enumerate(S)}

        ans = []
        start = 0
        end = 0
        while end < len(S):
            chars = set(S[start : end + 1])
            new_end = end
            for char in chars:
                last = lasts[char]
                if last > new_end:
                    new_end = last

            if new_end == end:
                ans.append(new_end - start + 1)
                start = new_end + 1
                end = new_end + 1
            else:
                end = new_end

        return ans

    def partitionLabels(self, S: str) -> List[int]:
        """Draft 1
        Two pointer solution, using rfind, can optimize rfind
        """
        if not S:
            return None

        ans = []
        start = 0
        end = 0
        while end < len(S):
            chars = set(S[start : end + 1])
            new_end = end
            for char in chars:
                last = S.rfind(char)
                if last > new_end:
                    new_end = last

            if new_end == end:
                ans.append(new_end - start + 1)
                start = new_end + 1
                end = new_end + 1
            else:
                end = new_end

        return ans
