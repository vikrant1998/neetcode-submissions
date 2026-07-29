class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class DLL:
    def __init__(self):
        self.length = 0
        self.head = None  # Least recently used
        self.tail = None  # Most recently used

    def insert_node(self, node: Node) -> None:
        node.prev = self.tail
        node.next = None

        if self.tail is not None:
            self.tail.next = node
        else:
            self.head = node

        self.tail = node
        self.length += 1

    def delete_node(self, node: Node) -> None:
        if node.prev is not None:
            node.prev.next = node.next
        else:
            self.head = node.next

        if node.next is not None:
            node.next.prev = node.prev
        else:
            self.tail = node.prev

        node.prev = None
        node.next = None
        self.length -= 1

    def move_to_tail(self, node: Node) -> None:
        if node is self.tail:
            return

        self.delete_node(node)
        self.insert_node(node)

    def remove_head(self) -> Node | None:
        if self.head is None:
            return None

        node = self.head
        self.delete_node(node)
        return node


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = dict()
        self.dll = DLL()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self.dll.move_to_tail(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.dll.move_to_tail(node)
            return

        node = Node(key, value)
        self.cache[key] = node
        self.dll.insert_node(node)

        if len(self.cache) > self.capacity:
            lru_node = self.dll.remove_head()
            del self.cache[lru_node.key]