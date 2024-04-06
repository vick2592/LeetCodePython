class Solution:
    def distributeCandies(candies, num_people):
        tempC = candies
        nList = [0 for x in range(num_people)]
        print(nList)
        cTrack = 1
        ind = 0
        while(tempC > 0):
            ind = ind % num_people
            if(tempC - cTrack < 0):
                rem = 0
                for i in range(num_people - 1):
                    rem += nList[i] 
                rem = candies - rem    
                nList[ind] += rem
                break
            nList[ind] += cTrack
            tempC -= cTrack
            cTrack += 1
            ind += 1
            print(cTrack)
        
        return nList
    
candies = 7
num_people = 4
        
ans = Solution.distributeCandies(candies, num_people)
print(ans)  # Output: [1,2,3,1]