class SORTracker:

    def __init__(self):
        self.scenes = []
        self.i = 0
        
    def add(self, name: str, score: int) -> None:
        self.scenes.append([name, score])

    def get(self) -> str:
        self.scenes.sort(key=lambda x: x[0])
        self.scenes.sort(key=lambda x: x[1], reverse = True)
        print(self.scenes[self.i])
        #print(self.i, self.scenes)
        self.i += 1
        return self.scenes[self.i - 1][0]

input = ["SORTracker", "add", "add", "get", "add", "get", "add", "get", "add", "get", "add", "get", "get"]
inputGuide = [[], ["bradford", 2], ["branford", 3], [], ["alps", 2], [], ["orland", 2], [], ["orlando", 3], [], ["alpine", 2], [], []]

# Your SORTracker object will be instantiated and called as such:
#obj = SORTracker()
#obj.add(inputGuide[1][0], inputGuide[1][1])
#param_2 = obj.get()
#print(param_2)

for i in range(len(input)):
    if input[i] == "SORTracker":
        obj = SORTracker()
    elif input[i] == "add":
        obj.add(inputGuide[i][0], inputGuide[i][1])
    elif input[i] == "get":
        param_2 = obj.get()