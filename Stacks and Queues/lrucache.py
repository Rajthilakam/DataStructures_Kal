from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.lruInfo = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.lruInfo:
            self.lruInfo.move_to_end(key)
            return self.lruInfo[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.lruInfo:
            if self.capacity >= 0:
                self.capacity -= 1
                
            if self.capacity < 0:
                self.lruInfo.popitem( last = False )
        
        self.lruInfo[key] =  value
        self.lruInfo.move_to_end(key)
        
obj = LRUCache(3)
param_1 = obj.get(1)
obj.put(1,10)
obj.put(2,20)
obj.put(3,30)
obj.put(4,40)
param_2 = obj.get(1)
