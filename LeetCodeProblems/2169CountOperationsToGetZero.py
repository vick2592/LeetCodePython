class Solution:
    def countOperations(num , num2):
        temp1 = num
        temp2 = num2
        count = 0
        while (temp1 != 0 and temp2 != 0):
            if temp1 > temp2:
                temp1 = temp1 - temp2
            else:
                temp2 = temp2 - temp1
            count += 1
        return count
    
num1 = 2
num2 = 3
ans = Solution.countOperations(num1, num2)
print(ans)
