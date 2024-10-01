from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()
        
    def get(self, key: int) -> int:
        # return value of key if it exists 
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        return -1 


    def put(self, key: int, value: int) -> None:
        # if key exists, update value 
        if key in self.cache:
            self.cache.move_to_end(key)
        
        # add the key 
        self.cache[key] = value
       
        # check the capcity 
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)