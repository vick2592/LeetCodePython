from asyncio.windows_events import NULL
from copy import deepcopy


class NumArray:

    def __init__(self, nums: []):
        self.numArray = deepcopy(nums)

    def sumRange(self, left: int, right: int) -> int:
        count = 0
        for x in range(left, right+1):
            count += self.numArray[x]
        
        return count

numList = [[-2, 0, 3, -5, 2, -1], [0, 2], [2, 5], [0, 5]]
ans = []
for x in range(len(numList)):
    if x == 0:
        numObj = NumArray(numList[x])
        ans.append(NULL)
    else:
        ans.append(numObj.sumRange(numList[x][0], numList[x][1]))
        
print(ans)
        
        

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)