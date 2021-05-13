from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Build trie
        trie = {}
        for word in strs:
            node = trie
            for char in word:
                if char not in node:
                    node[char] = {}
                    node = node[char]
                else:
                    node = node[char]
            node["."] = None

        # Output
        result = []
        node = trie
        while len(node) == 1:
            key = list(node.keys())[0]
            if key == ".":
                break

            result.append(key)
            node = node[key]
        return "".join(result)

    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for word in strs:
            if not prefix:
                break

            while prefix and word.find(prefix) != 0:
                prefix = prefix[:-1]
        return prefix
