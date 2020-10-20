class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        if not words:
            return True

        # init ordermap
        ordermap = {}
        for i, c in enumerate(order):
            ordermap[c] = i

        for i in range(len(words) - 1):
            word_1 = words[i]
            word_2 = words[i + 1]
            min_len = min(len(word_1), len(word_2))
            is_same = True  # flag if all letters within min_len are same
            for j in range(min_len):
                if ordermap[word_1[j]] < ordermap[word_2[j]]:
                    is_same = False
                    break
                elif ordermap[word_1[j]] > ordermap[word_2[j]]:
                    return False
                # If letters are same, do nothing

            # is_same check
            if is_same and len(word_1) > len(word_2):
                return False

        return True
