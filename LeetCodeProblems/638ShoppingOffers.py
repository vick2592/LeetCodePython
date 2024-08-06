class Solution:
    def shoppingOffers(price, special, needs):
        
        def shoppingOffersHelper(price, special, needs):
            if sum(needs) == 0:
                return 0
            minPrice = sum([price[i] * needs[i] for i in range(len(needs))])
            for s in special:
                newNeeds = [needs[i] - s[i] for i in range(len(needs))]
                if all([newNeeds[i] >= 0 for i in range(len(newNeeds))]):
                    minPrice = min(minPrice, s[-1] + shoppingOffersHelper(price, special, newNeeds))
            return minPrice
        
        return shoppingOffersHelper(price, special, needs)
    

price = [2,3,4]
special = [[1,1,0,4],[2,2,1,9]]
needs = [1,2,1]        
answer = Solution.shoppingOffers(price, special, needs)
print(answer)  # Expected output: 11