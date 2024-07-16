from copy import deepcopy

class Solution:
    def minimumAddedCoins(coins, target):
        def helper2(cLists, trg):
            queue = [cLists]
            while queue:
                cList = queue.pop(0)
                if sum(cList) == trg:
                    return True
                for i in range(len(cList)):
                    test = deepcopy(cList)
                    test.pop(i)
                    queue.append(test)
            return False
        
        origin = len(coins)
                    
        for i in range(1, target+1):
            if i in coins:
                continue
            else:
                if helper2(coins, i):
                    continue
                else:
                    coins.append(i)
                    
        return len(coins) - origin
    
coins = [1,4,10]
target = 19

answer = Solution.minimumAddedCoins(coins, target)
print(answer)  # Output: 0