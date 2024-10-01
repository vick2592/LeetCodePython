class SnapshotArray:

    def __init__(self, length):
        self.length = length
        self.snap_id = 0
        self.snapshots = []
        self.snapshots.append([0] * length)
        self.snapmap = {}
        self.snapmap[self.snap_id] = self.snapshots.copy()
        return
        

    def set(self, index, val):
        self.snapmap[self.snap_id][index] = val
        return
        

    def snap(self):
        self.snap_id += 1
        self.snapmap[self.snap_id] = self.snapshots[self.snap_id - 1].copy()
        #print(self.snap_id)
        return self.snap_id
        

    def get(self, index, snap_id):
        if snap_id in self.snapmap:
            return self.snapmap[snap_id][index]
        return 0
        


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)

# ["SnapshotArray","set","snap","set","get"]
# [[3],[0,5],[],[0,6],[0,0]]
obj = SnapshotArray(3)
obj.set(0, 5)
obj.snap()
obj.set(0, 6)
answer = obj.get(0, 0)
print(answer)  # Expected output: 5)