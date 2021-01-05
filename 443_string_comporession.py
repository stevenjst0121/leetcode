from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        """Draft 1
        Two pointer solution with O(1) space, beats 40%
        Solution is just more clean, and calls it read/write, but same big O
        """
        if not chars:
            return 0

        start, curr = 0, 1
        length = len(chars)
        count = 1
        while curr <= length:
            if curr == length or chars[curr - 1] != chars[curr]:
                # Handle previous char
                char = chars[curr - 1]
                chars[start] = char
                start += 1

                if count != 1:
                    num_chars = []
                    while count > 0:
                        num_chars.append(str(count % 10))
                        count //= 10
                    chars[start : start + len(num_chars)] = num_chars[::-1]
                    start += len(num_chars)

                # next?
                if curr == length:
                    break
                else:
                    # continue
                    count = 1
                    curr += 1
            else:
                count += 1
                curr += 1

        return start
