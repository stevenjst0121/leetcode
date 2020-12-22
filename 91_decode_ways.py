class Solution:
    def numDecodings(self, s: str) -> int:
        """Draft 2
        Dynamic programming bottom-up
        """
        if s[0] == "0":
            return 0

        i = len(s) - 1
        count = [0] * (len(s) + 1)
        count[len(s)] = 1
        count[i] = 0 if s[i] == "0" else 1
        i -= 1
        while i >= 0:
            if count[i + 1] == 0 and count[i + 2] == 0:
                break

            if s[i] == "0":
                count[i] = 0
                i -= 1
                continue

            count_1 = count[i + 1]
            count_2 = 0
            two_digit = int(s[i : i + 2])
            if two_digit <= 26:
                count_2 = count[i + 2]

            count[i] = count_1 + count_2
            i -= 1

        return count[0]

    def __init__(self):
        self.count = 0
        self.memo = {"": 1}  # string -> count

    def numDecodings(self, s: str) -> int:
        """Draft 1
        Recursion + memoization
        """
        if s in self.memo:
            return self.memo[s]

        if s[0] == "0":
            return 0
        if len(s) == 1:
            return 1

        # nex is not 0
        count_1 = self.numDecodings(s[1:])
        count_2 = 0
        two_digit = int(s[:2])
        if two_digit <= 26:
            count_2 = self.numDecodings(s[2:])
        count = count_1 + count_2
        self.memo[s] = count
        return count
