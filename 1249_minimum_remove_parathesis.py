class Solution:
    # TODO look into solution
    def minRemoveToMakeValid(self, s: str) -> str:
        """Draft 1
        Thoughts:
         - Define a isValid() function
         - First find count of ( and ) in string, and try to remove the ones that has extra
         (remove "(" from right and remove ")" from left)
         - Check if valid after removing extras. If still not valid, remove from both sides and continously checking
        """
        if not s or self.isValid(s):
            return s

        # Find total counts
        l_count = 0
        r_count = 0
        for c in s:
            if c == "(":
                l_count += 1
            if c == ")":
                r_count += 1

        # Start remove diff #
        diff = l_count - r_count
        if diff > 0:
            # ( is more, remove from right
            while diff > 0:
                l_index = s.rfind("(")
                s = s[:l_index] + s[l_index + 1 :]
                diff -= 1
        elif diff < 0:
            # ) is more, remove from left
            while diff < 0:
                r_index = s.find(")")
                s = s[:r_index] + s[r_index + 1 :]
                diff += 1
        else:
            # equal, do nothing
            pass

        # Check if valid
        if self.isValid(s):
            return s

        # Now ( and ) are balanced, remove from both side and keep checking
        count = min(l_count, r_count)
        while count > 0:
            l_index = s.rfind("(")
            s = s[:l_index] + s[l_index + 1 :]
            r_index = s.find(")")
            s = s[:r_index] + s[r_index + 1 :]

            if self.isValid(s):
                return s

        # All ()s are removed, return s
        return s

    def isValid(self, s: str) -> bool:
        if not s:
            return True

        l_count = 0
        for c in s:
            if c == "(":
                l_count += 1
            elif c == ")":
                if l_count == 0:
                    return False
                l_count -= 1
        return l_count == 0
