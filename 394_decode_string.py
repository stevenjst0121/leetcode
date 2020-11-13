from collections import deque


class Solution:
    def decodeString(self, s: str) -> str:
        """Draft 1
        [MEMO] Use single stack
        Was stuck at stack solution first because was thinking of storing only [ and ], but can actually store all
        """
        # Assume s must be in form of #[.*]
        ans = ""
        stack = deque()
        for i, c in enumerate(s):
            if c != "]":
                stack.append(c)
            else:
                # c == "]"
                subs = ""
                while stack[-1] != "[":
                    subs = stack.pop() + subs
                stack.pop()
                k = 0
                multi = 1
                while stack and stack[-1].isdigit():
                    k += multi * int(stack.pop())
                    multi *= 10
                decoded = subs * k
                stack.append(decoded)
        ans = "".join(list(stack))
        return ans
