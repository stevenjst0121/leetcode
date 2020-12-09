import heapq
from typing import *


def test_range():
    # for i in range(1, 1):
    #     print(i)

    # for i in range(2, 1):
    #     print(i)

    # for i in range(3, -1, -1):
    #     print(i)

    for k in range(0, 1):
        print(k)


def test_list():
    l = [1, 2, 3, 4, 5]
    l[1:1] = []
    print(l)


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def generate_list(list: List) -> ListNode:
    dummyHead = ListNode()
    curr = dummyHead
    for val in list:
        curr.next = ListNode(val)
        curr = curr.next
    return dummyHead.next


def list_pass_object_by_reference_while_looping():
    d1 = {1: "a"}
    d2 = {2: "b"}
    lists = [d1, d2]

    d = None
    for i in range(len(lists)):
        dd = lists[i]
        d = dd

    print(d is d1)
    print(d is d2)


def test_string_immutable():
    words = ["abc", "def"]
    for word in words:
        word = "***"
    print(words)


class Interval:
    def __init__(self, begin: int = 0, end: int = 0):
        self.begin = begin
        self.end = end

    def __lt__(self, other):
        return self.begin < other.begin

    def __repr__(self):
        return f"[{self.begin}, {self.end}]"

    def __hash__(self):
        return hash((self.begin, self.end))

    def __eq__(self, other):
        return self.begin == other.begin and self.end == other.end


def test_heapq():
    l = []
    heapq.heappush(l, Interval(1, 3))
    heapq.heappush(l, Interval(1, 2))
    heapq.heappush(l, Interval(2, 4))
    heapq.heappush(l, Interval(5, 8))
    heapq.heappush(l, Interval(7, 9))
    # print(l)

    l = [
        (65, 424),
        (351, 507),
        (314, 807),
        (387, 722),
        (19, 797),
        (259, 722),
        (165, 221),
        (136, 897),
    ]
    heapq.heapify(l)
    print(l)


def test_dict_hash():
    d = {}
    d[Interval(1, 3)] = "1,3"
    d[Interval(2, 4)] = "2,4"
    print(d)


def test_bit_manipulation():
    def get_bit(x: int) -> str:
        result = ""
        while int(x / 2):
            bit = x % 2
            result = str(bit) + result
            x = int(x / 2)

        if x % 2:
            result = "1" + result

        return result

    print(get_bit(1))
    print(get_bit(10))
    print(get_bit(100))


class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random
        self.l = [1, 2, 3]


def is_node_hashable():
    node_0 = Node(0)
    maps = {}
    maps[node_0] = 0
    node_1 = Node(0)
    maps[node_1] = 1
    assert len(maps) == 2
    assert maps[node_0] == 0
    assert maps[node_1] == 1


if __name__ == "__main__":
    # test_range()
    # list_pass_object_by_reference_while_looping()
    # test_string_immutable()
    # test_list()
    # test_heapq()
    # test_dict_hash()
    # test_bit_manipulation()
    is_node_hashable()
