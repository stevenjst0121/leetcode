from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        """No solution is available
        Nothing special here, just to make sure understand full justification
        The spaces should be distributed as evenly as possible, e,g:
        2,2,2,2
        2,2,1,1
        3,2,2,2
        """
        width = 0
        curr_words = []
        result = []
        for word in words:
            size = len(word)
            if width + size + len(curr_words) > maxWidth:
                line = self.fullJustifyLine(curr_words, maxWidth)
                result.append(line)
                width = size
                curr_words = [word]
            else:
                curr_words.append(word)
                width += size

        # Add last line
        line = self.leftJustifyLine(curr_words, maxWidth)
        result.append(line)
        return result

    def fullJustifyLine(self, words: List[str], maxWidth: int) -> str:
        words_len = sum([len(word) for word in words])
        words_count = len(words)
        space_needed = maxWidth - words_len

        if words_count == 1:
            return words[0] + " " * space_needed

        result = ""
        space_left = space_needed
        end = len(words) - 1
        for i, word in enumerate(words):
            if i == 0:
                result += word
            elif i == end:
                result += " " * space_left
                result += word
            else:
                words_left = end - i + 1
                is_even = space_left % words_left == 0
                if is_even:
                    space_to_add = space_left // words_left
                else:
                    space_to_add = (space_left // words_left) + 1
                result += " " * space_to_add
                space_left -= space_to_add
                result += word

        return result

    def leftJustifyLine(self, words: List[str], maxWidth: int) -> str:
        words_len = sum([len(word) for word in words])
        words_count = len(words)
        space_needed = maxWidth - words_len - words_count + 1
        result = ""
        for i, word in enumerate(words):
            if i == 0:
                result += word
            else:
                result += " "
                result += word
        result += " " * space_needed
        return result
