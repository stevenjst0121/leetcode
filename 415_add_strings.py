from collections import deque


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        sum = deque()
        p1 = len(num1) - 1
        p2 = len(num2) - 1
        carry_over = 0
        while p1 >= 0 or p2 >= 0:
            if p1 < 0:
                add = ord(num2[p2]) - ord("0") + carry_over
            elif p2 < 0:
                add = ord(num1[p1]) - ord("0") + carry_over
            else:
                add = ord(num2[p2]) - ord("0") + ord(num1[p1]) - ord("0") + carry_over
            sum.appendleft(add % 10)
            carry_over = int(add / 10)
            p1 -= 1
            p2 -= 1

        if carry_over:
            sum.appendleft(carry_over)

        return "".join([str(v) for v in sum])

    # def addStrings(self, num1: str, num2: str) -> str:
    #     """Draft 1
    #     Make num1 num2 same size by adding leading zeros
    #     """
    #     len_1 = len(num1)
    #     len_2 = len(num2)
    #     if len_1 > len_2:
    #         diff = len_1 - len_2
    #         num2 = "0" * diff + num2
    #     elif len_1 < len_2:
    #         diff = len_2 - len_1
    #         num1 = "0" * diff + num1

    #     carry_over = 0
    #     sum = deque()

    #     for i in range(max(len_1, len_2) - 1, -1, -1):
    #         add = int(num1[i]) + int(num2[i]) + carry_over
    #         sum.appendleft(str(add % 10))
    #         carry_over = int(add / 10)

    #     if carry_over:
    #         sum.appendleft(str(carry_over))

    #     return "".join(list(sum))
