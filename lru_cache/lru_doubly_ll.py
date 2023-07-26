from collections import OrderedDict


class DLNode:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.next = None
        self.prev = None


class DLList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, node):
        if not self.head and not self.tail:
            self.head = node
            self.tail = node
        else:
            self.tail.prev = node
            node.next = self.tail
            self.tail = node

    def pophead(self):
        if self.head:
            old_head = self.head
            self.head = old_head.prev
            if self.head:
                self.head.next = None
                old_head.prev = None
            else:
                self.tail = None
            return old_head

        return None

    def move_to_end(self, node):
        if self.tail == node and self.head == node:
            return

        # disconnect node from its prev and next
        nn = node.next
        np = node.prev
        if nn:
            nn.prev = np
            if np:
                np.next = nn
            else:
                self.tail = nn
        else:
            self.head = np
            if np:
                np.next = None
            else:
                self.tail = None
        # move node to tail
        node.next = self.tail
        self.tail.prev = node
        node.prev = None
        self.tail = node



class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.values = DLList()
        self.keys = dict()

    def get(self, key: int) -> int:
        if key in self.keys:
            node = self.keys[key]
            self.values.move_to_end(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.keys:
            if len(self.keys) == self.cap:
                head = self.values.pophead()
                del self.keys[head.key]
            new_node = DLNode(key, value)
            self.values.append(new_node)
            self.keys[key] = new_node
        else:
            node = self.keys[key]
            node.val = value
            self.values.move_to_end(node)