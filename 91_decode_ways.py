class Solution:
    def numDecodings(self, s: str) -> int:
        """Dynamic programming
        [MEMO] Bottom-up solution, for this one needs to build from the right
        because leading zeros are not valid
        """
        if s[0] == "0":
            return 0

        N = len(s)
        ways = [0] * (N + 1)
        ways[N] = 1
        ways[N - 1] = 0 if s[N - 1] == "0" else 1
        for i in range(N - 2, -1, -1):
            if s[i] == "0":
                ways[i] = 0
                continue

            ways_1 = ways[i + 1]
            ways_2 = 0
            two_digits = int(s[i : i + 2])
            if two_digits <= 26:
                ways_2 = ways[i + 2]
            ways[i] = ways_1 + ways_2

        return ways[0]
