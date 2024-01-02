class LRUCache:

    def __init__(self, capacity: int):
        self.queue = []
        self.capacity = capacity
        self.cache = {}

    def get(self, key: int) -> int:
        if key in self.cache:
            self.queue.remove(key)
            self.queue.append(key)
            return self.cache[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key] = value
            self.queue.remove(key)
            self.queue.append(key)
        if key not in self.cache:
            self.cache[key] = value
            self.queue.append(key)
            if len(self.queue) > self.capacity:
                poped_val = self.queue.pop(0)
                self.cache.pop(poped_val)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)