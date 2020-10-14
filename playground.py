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


if __name__ == "__main__":
    # test_range()
    # list_pass_object_by_reference_while_looping()
    # test_string_immutable()
    test_list()