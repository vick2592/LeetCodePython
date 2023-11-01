class FreqStack:
    
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> int:
        val = self.stack.pop()
        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()

inputs = ["FreqStack", "push", "push", "push", "push", "push", "push", "pop", "pop", "pop", "pop"]
inputVal = [[], [5], [7], [5], [7], [4], [5], [], [], [], []]

for x in range(len(inputs)):
    if inputs[x] == "FreqStack":
        obj = FreqStack()
    elif inputs[x] == "push":
        obj.push(inputVal[x][0])
    elif inputs[x] == "pop":
        param_2 = obj.pop()
        print(param_2)