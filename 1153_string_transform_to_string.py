class Solution:
    def canConvert(self, str1: str, str2: str) -> bool:
        """Solution super simple
        [MEMO]
        Seems like a graph problem but is a bit different
        Each node in this graph is only allowed to have 1 child, which makes the following super simple solution
        """
        if len(set(str2)) == 26:
            return str1 == str2
        d = {}
        for i in range(len(str1)):
            if str1[i] in d:
                if d[str1[i]] != str2[i]:
                    return False
            else:
                d[str1[i]] = str2[i]
        return True