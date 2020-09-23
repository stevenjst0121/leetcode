from collections import deque


class Solution:
    # def reorderSpaces(self, text: str) -> str:
    #     """
    #     Use list, O(N)
    #     """
    #     l = text.split()
    #     count = 0
    #     for c in text:
    #         if c == " ":
    #             count = count + 1

    #     if len(l) < 2:
    #         return l[0] + " " * count

    #     number = int(count / (len(l) - 1))
    #     res = count % (len(l) - 1)

    #     result = (" " * number).join(l)
    #     result = result + (" " * res)
    #     return result

    def reorderSpaces(self, text: str) -> str:
        l = []
        start = -1  # postion of first nonspace char
        count = 0  # count of spaces
        for i, char in enumerate(text):
            if char == " ":
                if start < i and start >= 0:
                    s = text[start:i]
                    l.append(s)
                    start = -1  # reset start

                count = count + 1
            else:
                if start < 0:
                    start = i
                elif i == len(text) - 1:
                    # last word no trailing spaces
                    s = text[start:]
                    l.append(s)
                    break

        if len(l) < 2:
            return l[0] + " " * count

        number = int(count / (len(l) - 1))
        res = count % (len(l) - 1)

        result = (" " * number).join(l)
        result = result + (" " * res)
        return result


if __name__ == "__main__":
    s = Solution()
    # text = "  this   is  a sentence "
    text = " practice   makes   perfect"
    # text = "hello   world"
    # text = "  walks  udp package   into  bar a"
    # text = "   hello"
    result = s.reorderSpaces(text)
    print(f"'{result}'")
