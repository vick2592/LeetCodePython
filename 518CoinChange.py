from functools import cache

#In the given solution, the change_method_count array is used to store the number of ways to make a given amount of money using the given coins. 
#The change_method_count[i] element represents the number of ways to make amount i using the given coins.

#The solution first initializes change_method_count to be a list with amount+1 elements, where the first element is set to 1 
#(representing the number of ways to make amount 0, which is 1) and the remaining elements are set to 0.

#Then, the solution iterates over the coins in the coins list and updates the change_method_count array to reflect the number of ways to make each amount of money
#using the current coin.

#In each iteration, the solution looks at the small amounts of money first and then works its way up to larger amounts. This is done by iterating over the small_amounts in 
#the range range(cur_coin, amount+1), where cur_coin is the value of the current coin being considered.

#This is done because it is necessary to consider the smaller amounts of money first in order to correctly calculate the number of ways to make the larger amounts of money.

#For example, if we are considering the coin value 5 and we want to calculate the number of ways to make amount 10, we need to first consider the number of ways to make 
#the smaller amounts of money, such as amount 5. This is because the number of ways to make amount 10 will depend on the number of ways to make the smaller amounts of money, 
#such as amount 5.

#In this way, by starting with the small amounts of money and working our way up to the larger amounts, we are able to correctly calculate the number of ways to make the 
#desired amount of money, which is the value of change_method_count[amount] at the end of the solution.

#I hope this helps to clarify the reason for considering the small amounts of money first in the given solution. Please let me know if you have any further questions.

#Bottom Up dynamic programing solution
class Solution:
    def change(amount, coins):
        # base case:
        # amount 0's method count = 1 (by taking no coins)
        change_method_count = [1] + [ 0 for _ in range(amount)]
        
        # make change with current coin, from small coin to large coin
        for cur_coin in coins:
            
            # update change method count from small amount to large amount
            for small_amount in range(cur_coin, amount+1):
                
                # current small amount can make changed with current coin
                change_method_count[small_amount] += change_method_count[small_amount - cur_coin]
                
        return change_method_count[amount]

amount = 5
coins = [1,2,5]

coins.sort(reverse = True)
print(coins)
coins.sort(reverse = False)
print([0]*3)
answer = Solution.change(amount, coins)
print(answer)
print(list(range(3,3)))

#Note nothing prints when the range is 3,3 for example. Also the for loop does not execute under that range since its is None or 3 to 3 not including 3.
for _ in range(3,4):
    print("Does this even print to screen?")

#Top-down dynamic Programming Solution with Recursion
class Solution2:
    def change(amount, coins):
        
        # use python build-in cache as memoization for DP
        @cache
        def dpf(money, coin_idx):
            
            #  Input: 
            #         money to change
            #         current coin index, stands for coins[coin_idx]
                
            #  Output: total combination of change for money

            if money == 0:
                
                # $0 = taking no coins, only one way to do so
                return 1
            
            elif coin_idx < 0:
                # Cannot change without coins
                return 0
            
            if money < coins[coin_idx]:
                
                # money is smaller than current coin
                # method count = change without current coin
                return dpf(money, coin_idx-1)
            
            else:
                # money is larger than or equal to current coin
                # method count = change without current coin + change with current coin
                return dpf(money, coin_idx-1) + dpf(money - coins[coin_idx], coin_idx)
            
        # ----------------------------------------------------------
        last_coin_idx = len(coins) - 1
        return dpf(amount, last_coin_idx)

answer2 = Solution2.change(amount, coins)
print(answer2)