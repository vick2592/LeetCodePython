class MyHashMap:

    def __init__(self):
        self.map = {}


    def put(self, key: int, value: int) -> None:
        self.map[key] = value


    def get(self, key: int) -> int:
        if(key in self.map.keys()):
            return self.map[key]
        else:
            return -1

    def remove(self, key: int) -> None:
        if(key in self.map.keys()):
            self.map.pop(key)
        


# Your MyHashMap object will be instantiated and called as such:

obj = MyHashMap()
obj.put(1,1)
obj.put(2,2)
param_2 = obj.get(1)
print(param_2)
obj.put(2,1)
param_3 = obj.get(2)
print(param_3)
obj.remove(2)
param_4 = obj.get(2)
print(param_4)