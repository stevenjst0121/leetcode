from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity: int):
        """Solution 1
        [MEMO] Directly use OrderedDict move_to_end and popitem
        """
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key] = value
            self.cache.move_to_end(key)
            return

        if len(self.cache) == self.capacity:
            self.cache.popitem(False)

        self.cache[key] = value


class LRUCache:
    """Use double linked list to implement self
    [MEMO] Use start - end node when implementing linked list
    _add_node - always add at front
    _remove_node
    _move_to_head - implement use _add_node and _remove_node
    _pop_tail
    [MEMO] Tips - The sequence of modifing links matter, start from one node, put the longer ones first
    """

    class Node:
        def __init__(self, key, val):
            self.key = key
            self.val = val
            self.prev = None
            self.next = None

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.cache = {}  # key to Node
        self.head = LRUCache.Node(0, 0)
        self.tail = LRUCache.Node(0, 0)

        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        self._move_to_head(self.cache[key])

        return self.cache[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].val = value
            self._move_to_head(self.cache[key])
            return

        node = LRUCache.Node(key, value)
        self.cache[key] = node
        self._add_node(node)
        self.size += 1

        if self.size > self.capacity:
            # remove lru key
            node = self._pop_tail()
            del self.cache[node.key]
            self.size -= 1

    def _add_node(self, node):
        """
        Always add the new node right after head.
        """
        node.prev = self.head
        node.next = self.head.next

        # [MEMO] This must run first!
        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node):
        """
        Remove an existing node from the linked list.
        """
        prev = node.prev
        new = node.next

        prev.next = new
        new.prev = prev

    def _move_to_head(self, node):
        """
        Move certain node in between to the head.
        """
        self._remove_node(node)
        self._add_node(node)

    def _pop_tail(self):
        res = self.tail.prev
        self._remove_node(res)
        return res
