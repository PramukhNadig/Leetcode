class Node:
    def __init__(self, key, value, prev=None, next=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next
        
class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.lru = None
        self.mru = None
        self.dict = {}
        self.size = 0

    def get(self, key: int) -> int:
        node = self.dict.get(key, None)
        if not node:
            return -1
            
        if node is self.mru:
            return node.value
        elif node is self.lru:
            self.lru = self.lru.next
            self.lru.prev = None
            
            self.mru.next = node
            node.prev = self.mru
            node.next = None
            self.mru = node
            return node.value
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            
            self.mru.next = node
            node.prev = self.mru
            node.next = None
            self.mru = node
            return node.value
                
                
    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            self.get(key)
            self.mru.value = value
            return
            
        if not self.mru:
            self.mru = Node(key, value)                 
            self.lru = self.mru
            self.dict[key] = self.mru
            self.size += 1
            return
        
        if self.size == self.cap:
            lruKey = self.lru.key
            self.get(lruKey)
            self.dict.pop(lruKey, None)
            
            self.mru.key = key
            self.mru.value = value
            self.dict[key] = self.mru
        else:
            self.mru = Node(key, value, prev=self.mru)
            self.dict[key] = self.mru
            self.mru.prev.next = self.mru
            self.size += 1
                        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
