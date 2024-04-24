class Solution:
    def fillCups(amount):
        total = sum(amount)
        if total % 2 >= 1:
            ans = total // 2 + 1
            return ans
        else:
            return total // 2
    
amount = [1,4,2]
print(Solution.fillCups(amount)) # 2
