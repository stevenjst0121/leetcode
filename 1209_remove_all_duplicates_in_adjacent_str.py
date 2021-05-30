class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        counts = []
        for c in s:
            if not stack or c != stack[-1]:
                counts.append(1)
                stack.append(c)
                continue

            # c == stack[-1]
            if counts[-1] == k - 1:
                counts.pop()
                for _ in range(k - 1):
                    stack.pop()
            else:
                counts[-1] += 1
                stack.append(c)
        return "".join(stack)

    def removeDuplicates(self, s: str, k: int) -> str:
        """Solution using stack to keep track of count
        [MEMO] This will avoid recursion but keep removing substrings until done
        Since string length will be changed during iteration, make sure to use
        while i < len(s)

        See above solution for a more intuitive design with the help of a stack
        """
        counts = []
        i = 0
        while i < len(s):
            if i == 0 or s[i] != s[i - 1]:
                counts.append(1)
                i += 1
                continue

            counts[-1] += 1
            if counts[-1] == k:
                counts.pop()
                s = s[: i - k + 1] + s[i + 1 :]
                i -= k
            i += 1
        return s

    def removeDuplicates(self, s: str, k: int) -> str:
        """Draft 2
        Use builder as stack to build from 0 and keep track of count, beats 28%
        """
        if len(s) == 1:
            return s

        if k > len(s):
            return s

        builder = [s[0]]
        count = 1
        for i in range(1, len(s)):
            builder.append(s[i])
            if s[i] == s[i - 1]:
                count += 1
            else:
                count = 1

            if count == k:
                del builder[-k:]
        new_s = "".join(builder)
        if new_s == s:
            return s
        else:
            return self.removeDuplicates(new_s, k)

    def removeDuplicates(self, s: str, k: int) -> str:
        """Draft 1
        Recursive two pointer solution, but only beats 5%
        """
        if len(s) == 1:
            return s

        if k > len(s):
            return s

        i, j = 0, k - 1
        pre = 0
        builder = []
        while j < len(s):
            if s[i] == s[j] and all(s[l] == s[i] for l in range(i, j)):
                builder.append(s[pre:i])
                pre = j + 1
                i += k
                j += k
            else:
                i += 1
                j += 1

        if pre == 0:
            return s

        builder.append(s[pre:])
        new_s = "".join(builder)
        return self.removeDuplicates(new_s, k)
