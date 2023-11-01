from itertools import combinations

class CombinationIterator:
    combinationList = []
    def __init__(self, characters: str, combinationLength: int):
        CombinationIterator.combinationList = list(combinations(characters, combinationLength))
        print(CombinationIterator.combinationList)

    def next(self):
        if(len(CombinationIterator.combinationList) < 1):
            print("no more next")
            return
        if(CombinationIterator.combinationList[0]):
            print("Current next value: ", CombinationIterator.combinationList[0])
            CombinationIterator.combinationList.pop(0)
            print("Current list after pop: ", CombinationIterator.combinationList)


    def hasNext(self):
        if(len(CombinationIterator.combinationList) > 0):
            print(CombinationIterator.combinationList[0])
            print(True)
            return
        print(False)

# Your CombinationIterator object will be instantiated and called as such:
characters = "abc"
combinationLength = 2
obj = CombinationIterator(characters, combinationLength)
param_1 = obj.next()
param_2 = obj.hasNext()
param_3 = obj.next()
param_4 = obj.hasNext()
param_5 = obj.next()
param_6 = obj.hasNext()