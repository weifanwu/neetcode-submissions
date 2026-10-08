class Node:

    def __init__(self, key=None, val=None):
        self.val = val
        self.key = key
        self.next = None
        self.previous = None


class LRUCache:

    def __init__(self, capacity: int):
        self.left, self.right = Node(), Node()
        self.left.next, self.right.previous = self.right, self.left
        self.capacity = capacity
        self.cache = {}
        self.total = 0

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.top(key)
        return self.cache[key].val

    def top(self, key: int) -> None:
        node = self.cache[key]
        node.previous.next = node.next
        node.next.previous = node.previous
        node.previous = self.left
        node.next = self.left.next
        self.left.next = node
        node.next.previous = node

    def removeOld(self) -> None:
        node = self.right.previous
        node.previous.next = node.next
        node.next.previous = node.previous
        del self.cache[node.key]

    def add(self, node: Node) -> None:
        node.next = self.left.next
        node.next.previous = node
        self.left.next = node
        node.previous = self.left

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            node = Node(key, value)
            self.cache[key] = node
            self.add(node)
            self.total += 1
        else:
            self.cache[key].val = value
            self.top(key)
        
        if self.capacity < self.total:
            self.removeOld()
            self.total -= 1