from collections import deque


class Solution:
    def calculate(self, s: str) -> int:
        """Solution 1
        [MEMO+1] Brilliant solution using stack
        """
        stack = []
        prev_op = "+"
        num = 0
        for i, c in enumerate(s):
            if c.isdigit():
                num = num * 10 + int(c)

            if not c.isdigit() and c != " " or i == len(s) - 1:
                if prev_op == "+":
                    stack.append(num)
                elif prev_op == "-":
                    stack.append(-1 * num)
                elif prev_op == "*":
                    prev = stack.pop()
                    num = prev * num
                    stack.append(num)
                elif prev_op == "/":
                    prev = stack.pop()
                    num = prev // num
                    stack.append(num)
                num = 0
                prev_op = c
        return sum(stack)

    def calculate(self, s: str) -> int:
        """Solution 2
        [MEMO] Brilliant solution without using stack
        """
        if not s:
            return 0

        result = 0
        last_num = 0
        current_num = 0
        operation = "+"
        for i, c in enumerate(s):
            if c.isdigit():
                current_num = current_num * 10 + int(c)

            if not c.isdigit() and c != " " or i == len(s) - 1:
                if operation == "+" or operation == "-":
                    result += last_num
                    last_num = current_num if operation == "+" else (-1 * current_num)
                elif operation == "+":
                    last_num += current_num
                elif operation == "*":
                    last_num *= current_num
                elif operation == "/":
                    last_num = int(last_num / current_num)

                operation = c
                current_num = 0

        result += last_num
        return result

    # def calculate(self, s: str) -> int:
    #     """Draft 1
    #     Idea is to define one function that calculates s that only contains * and /
    #     And another function that utlizes the above function to calculate entire string
    #     """
    #     s = s.replace(" ", "")
    #     return self.calculatePM(s)

    # def calculatePM(self, s: str) -> int:
    #     result = None
    #     mid = 0
    #     for i, c in enumerate(s):
    #         if c == "+" or c == "-":
    #             if mid == 0:
    #                 result = self.calculateMD(s[:i])
    #             else:
    #                 second = self.calculateMD(s[mid + 1 : i])
    #                 if s[mid] == "+":
    #                     result += second
    #                 elif s[mid] == "-":
    #                     result -= second
    #                 else:
    #                     print(f"ERROR - {s}")
    #                     exit(1)
    #             mid = i

    #     if mid > 0:
    #         second = self.calculateMD(s[mid + 1 :])
    #         if s[mid] == "+":
    #             result += second
    #         elif s[mid] == "-":
    #             result -= second
    #         else:
    #             print(f"ERROR - {s}")
    #             exit(1)
    #     else:
    #         result = self.calculateMD(s)

    #     return result

    # def calculateMD(self, s: str) -> int:
    #     # s should only contain * or / operators or none
    #     if "*" not in s and "/" not in s:
    #         return int(s)

    #     result = None
    #     mid = 0
    #     for i, c in enumerate(s):
    #         if c == "*" or c == "/":
    #             if mid == 0:
    #                 result = int(s[:i])
    #             else:
    #                 second = int(s[mid + 1 : i])
    #                 if s[mid] == "*":
    #                     result *= second
    #                 elif s[mid] == "/":
    #                     result //= second
    #                 else:
    #                     print(f"ERROR - {s}")
    #                     exit(1)
    #             mid = i

    #     if mid > 0:
    #         second = int(s[mid + 1 :])
    #         if s[mid] == "*":
    #             result *= second
    #         elif s[mid] == "/":
    #             result //= second
    #         else:
    #             print(f"ERROR - {s}")
    #             exit(1)
    #     else:
    #         result = int(s)

    #     return result
