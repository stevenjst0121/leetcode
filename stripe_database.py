import json
from typing import Dict, List


class Solution:
    # https://www.1point3acres.com/bbs/thread-672631-1-1.html
    # https://www.1point3acres.com/bbs/thread-571024-1-1.html
    # https://www.1point3acres.com/bbs/thread-551655-1-1.html
    # https://www.1point3acres.com/bbs/thread-469979-1-1.html
    # https://www.1point3acres.com/bbs/thread-451838-1-1.html
    # https://drive.google.com/file/d/1MMxv6-M5fdlqAzWKdfk2Jq91oLBSYQme/view

    def min_by_column(self, table: List, col: str) -> Dict:
        # result = None
        # min_val = float("Inf")
        # for row in table:
        #     val = row[col] if col in row else 0

        #     if val < min_val:
        #         result = row
        #         min_val = val

        # return result

        return self.first_by_key(table, "asc", col)

    def first_by_key(self, table: List, direction: str, col: str) -> Dict:
        if not table:
            return None

        if direction == "asc":
            table.sort(key=lambda row: row[col] if col in row else 0)
        elif direction == "desc":
            table.sort(key=lambda row: -1 * row[col] if col in row else 0)

        return table[0]

    def min_by_order(self, table: List, cols: List[str]) -> Dict:
        if not table:
            return None

        def get_sort_key(row):
            result = []
            for col in cols:
                if col not in row:
                    result.append(0)
                else:
                    result.append(row[col])
            return result

        table.sort(key=get_sort_key)

        return table[0]


def test_min_by_col():
    solution = Solution()

    table = [{"a": 1}, {"a": 2}, {"a": 3}]
    assert solution.min_by_column(table, "a") == {"a": 1}

    table = [{"a": 1, "b": 2}, {"a": 2}]
    assert solution.min_by_column(table, "a") == {"a": 1, "b": 2}

    table = [{"a": 2}, {"a": 1, "b": 2}]
    assert solution.min_by_column(table, "a") == {"a": 1, "b": 2}

    table = [{"a": 1}, {"b": 2}]
    assert solution.min_by_column(table, "a") == {"b": 2}

    table = []
    assert solution.min_by_column(table, "b") is None

    table = [{}]
    assert solution.min_by_column(table, "a") == {}


def test_first_by_key():
    solution = Solution()

    table = [{"a": 1}, {"a": 2}, {"a": 3}]
    assert solution.first_by_key(table, "asc", "a") == {"a": 1}
    assert solution.first_by_key(table, "desc", "a") == {"a": 3}

    table = [{"a": 1, "b": 2}, {"a": 2}]
    assert solution.first_by_key(table, "asc", "a") == {"a": 1, "b": 2}
    assert solution.first_by_key(table, "desc", "a") == {"a": 2}

    table = [{"a": 2}, {"a": 1, "b": 2}]
    assert solution.first_by_key(table, "asc", "a") == {"a": 1, "b": 2}
    assert solution.first_by_key(table, "desc", "a") == {"a": 2}

    table = [{"a": 1}, {"b": 2}]
    assert solution.first_by_key(table, "asc", "a") == {"b": 2}
    assert solution.first_by_key(table, "desc", "a") == {"a": 1}

    table = []
    assert solution.first_by_key(table, "asc", "a") is None
    assert solution.first_by_key(table, "desc", "a") is None

    table = [{}]
    assert solution.first_by_key(table, "asc", "a") == {}
    assert solution.first_by_key(table, "desc", "a") == {}


def test_min_by_order():
    solution = Solution()

    table = [{"a": 1, "b": 1}, {"a": 1, "b": 2}]
    assert solution.min_by_order(table, ["a", "b"]) == {"a": 1, "b": 1}

    table = [{"a": 1, "b": 1}, {"a": 1}]
    assert solution.min_by_order(table, ["a", "b"]) == {"a": 1}

    table = [{"a": 1, "b": 1}, {"a": 2, "b": 2}, {"a": 2, "b": 3}]
    assert solution.min_by_order(table, ["a", "b"]) == {"a": 1, "b": 1}

    table = [{"a": 1, "b": 2, "c": 3}, {"a": 1, "b": 2, "c": 4}]
    assert solution.min_by_order(table, ["a", "b", "c"]) == {"a": 1, "b": 2, "c": 3}

    table = [{"a": 1, "b": 3, "c": 2}, {"a": 2, "b": 1, "c": 1}]
    assert solution.min_by_order(table, ["a", "b"]) == {"a": 1, "b": 3, "c": 2}
    assert solution.min_by_order(table, ["a", "b", "c"]) == {"a": 1, "b": 3, "c": 2}
