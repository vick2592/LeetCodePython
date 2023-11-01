class Solution:
    def findRestaurant(list1, list2):
        wordDict = {}
        for x in range(len(list1)):
            for y in range(len(list2)):
                if( list1[x] == list2[y]):
                    wordDict[list1[x]] = x + y
                    
        print(wordDict)
        print("list: ", list(wordDict.items()))
        tempList = list(wordDict.items())
        tempList = sorted(tempList, key = lambda x: x[1])
        answerList = []
        tempInd = tempList[0][1]
        for pair in tempList:
            if pair[1] == tempInd:
                answerList.append(pair[0])
        return answerList
list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]

list1 = ["happy","sad","good"]
list2 = ["sad","happy","good"]
        
answer = Solution.findRestaurant(list1, list2)

print(answer)