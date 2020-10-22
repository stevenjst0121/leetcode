from collections import deque


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        """Solution 1
        Use stack to keep track of last (
        [MEMO] Use union on set
        [MEMO] String builder implementation
        """
        stack = deque()
        to_remove = set()
        for i, c in enumerate(s):
            if c == "(":
                stack.append(i)
            elif c == ")":
                if stack:
                    stack.pop()
                else:
                    to_remove.add(i)

        to_remove = to_remove.union(set(stack))
        string_builder = []
        for i, c in enumerate(s):
            if i not in to_remove:
                string_builder.append(c)
        return "".join(string_builder)

    # def minRemoveToMakeValid(self, s: str) -> str:
    #     """Solution 3
    #     Build string while looping
    #     """
    #     # First round remove all invalid ")"
    #     first_parse_chars = []
    #     balance = 0
    #     open_seen = 0
    #     for c in s:
    #         if c == "(":
    #             balance += 1
    #             open_seen += 1
    #         elif c == ")":
    #             if balance == 0:
    #                 continue
    #             balance -= 1

    #         first_parse_chars.append(c)

    #     # Check balance
    #     if balance == 0:
    #         return "".join(first_parse_chars)

    #     # Second round remove all invalid "(" from right
    #     result = []
    #     open_to_keep = open_seen - balance
    #     for c in first_parse_chars:
    #         if c != "(":
    #             result.append(c)

    #         if c == "(" and open_to_keep > 0:
    #             result.append(c)
    #             open_to_keep -= 1
    #     return "".join(result)

    # def minRemoveToMakeValid(self, s: str) -> str:
    #     """Draft 1
    #     Thoughts:
    #      - Define a isValid() function
    #      - First find count of ( and ) in string, and try to remove the ones that has extra
    #      (remove "(" from right and remove ")" from left)
    #      - Check if valid after removing extras. If still not valid, remove from both sides and continously checking
    #     """
    #     if not s or self.isValid(s):
    #         return s

    #     # Find total counts
    #     l_count = 0
    #     r_count = 0
    #     for c in s:
    #         if c == "(":
    #             l_count += 1
    #         if c == ")":
    #             r_count += 1

    #     # Start remove diff #
    #     diff = l_count - r_count
    #     if diff > 0:
    #         # ( is more, remove from right
    #         while diff > 0:
    #             l_index = s.rfind("(")
    #             s = s[:l_index] + s[l_index + 1 :]
    #             diff -= 1
    #     elif diff < 0:
    #         # ) is more, remove from left
    #         while diff < 0:
    #             r_index = s.find(")")
    #             s = s[:r_index] + s[r_index + 1 :]
    #             diff += 1
    #     else:
    #         # equal, do nothing
    #         pass

    #     # Check if valid
    #     if self.isValid(s):
    #         return s

    #     # Now ( and ) are balanced, remove from both side and keep checking
    #     count = min(l_count, r_count)
    #     while count > 0:
    #         l_index = s.rfind("(")
    #         s = s[:l_index] + s[l_index + 1 :]
    #         r_index = s.find(")")
    #         s = s[:r_index] + s[r_index + 1 :]

    #         if self.isValid(s):
    #             return s

    #     # All ()s are removed, return s
    #     return s

    # def isValid(self, s: str) -> bool:
    #     if not s:
    #         return True

    #     l_count = 0
    #     for c in s:
    #         if c == "(":
    #             l_count += 1
    #         elif c == ")":
    #             if l_count == 0:
    #                 return False
    #             l_count -= 1
    #     return l_count == 0
