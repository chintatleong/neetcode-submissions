# Definition for doubly-linked list.
class Node:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev
        
class LRUCache:

    def __init__(self, capacity: int):
        self.lru = {}       # key = key, value = node
        self.left = Node()
        self.right = Node()
        self.capacity = capacity

        self.left.next = self.right
        self.right.prev = self.left
        

    def get(self, key: int) -> int:
        value = -1
        
        if key in self.lru:
            # get value
            target = self.lru[key]
            k, value = target.val

            # update order
            # remove from the middle
            right = target.next
            left = target.prev

            left.next = right
            right.prev = left

            # place prev of self.right
            l = self.right.prev
            r = self.right

            target.prev = l 
            l.next = target
            target.next = r
            r.prev = target 

        return value

        

    def put(self, key: int, value: int) -> None:
        if key in self.lru:
            node = self.lru[key]
            node.val = (key, value)

            # remove node from nodes
            l = node.prev
            r = node.next
            # close the gap
            l.next = r
            r.prev = l

            # put new
            l = self.right.prev
            r = self.right
            l.next = node
            r.prev = node
            return


        if len(self.lru) >= self.capacity:
            # remove lru from nodes
            lru = self.left.next
            l = lru.prev
            r = lru.next
            # close the gap
            l.next = r
            r.prev = l

            # remove lru from dict
            k, v = lru.val
            del self.lru[k]

            # put new
            l = self.right.prev
            r = self.right
            node = self.lru[key] = Node((key,value), l, r)
            l.next = node
            r.prev = node
        

        else:
            l = self.right.prev
            r = self.right
            node = self.lru[key] = Node((key,value), l, r)

            l.next = node
            r.prev = node







        
