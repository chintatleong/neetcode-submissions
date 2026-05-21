class Node:
    def __init__(self, key, val):
        # Node can store key-value and previous and next pointers
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.left = Node(0,0)
        self.right = Node (0,0)
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node) -> None:
        prev = node.prev
        nxt = node.next
        
        prev.next = nxt
        nxt.prev = prev

    def insert(self, node) -> None:
        recent = self.right.prev

        recent.next = node
        node.prev = recent
        self.right.prev = node
        node.next = self.right


    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key] 
            self.remove(node)
            self.insert(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key] 
            node.val = value
            self.remove(node)
            self.insert(node)
        else:
            if (len(self.cache) < self.capacity):
                node = Node(key, value)
                self.cache[key] = node

                prev, nxt = self.right.prev, self.right

                prev.next = node
                nxt.prev = node
                node.next = nxt
                node.prev = prev

            else: 
                lru = self.left.next

                del self.cache[lru.key]
                self.remove(lru)

                node = Node(key, value)
                self.cache[key] = node
                self.insert(node)

        


            
