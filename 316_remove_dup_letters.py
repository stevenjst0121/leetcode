from collections import Counter


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # [MEMO]
        # Need to understand the problem, what's the strategy to pick one letter at a time
        c = Counter(s)
        pos = 0
        for i in range(len(s)):
            if s[i] < s[pos]:
                pos = i
            c[s[i]] -= 1
            if c[s[i]] == 0:
                break

        return s[pos] + self.removeDuplicateLetters(s[pos + 1 :].replace(s[pos], "")) if s else ""

    def removeDuplicateLetters(self, s: str) -> str:
        # [MEMO]
        # Brillliant usage of a stack, strategy is hard to think of
        stack = []
        seen = set()
        lasts = {c: i for i, c in enumerate(s)}

        for i, c in enumerate(s):
            if c not in seen:
                while stack and c < stack[-1] and lasts[stack[-1]] > i:
                    seen.remove(stack.pop())
                stack.append(c)
                seen.add(c)
        return "".join(stack)
