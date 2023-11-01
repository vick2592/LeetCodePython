class Solution:
    def maximumWealth(accounts):
        maxValue = 0
        for account in accounts:
            temp = 0
            for n in account:
                temp += n
            if temp > maxValue:
                maxValue = temp
                
        return maxValue
        

accounts = [[2,8,7],[7,1,3],[1,9,5]]
answer = Solution.maximumWealth(accounts)
print(answer)