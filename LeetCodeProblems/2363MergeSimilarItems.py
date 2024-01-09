class Solution:
    def mergeSimilarItems(items1, items2):
        ans = []
        if len(items1) >= len(items2):
            for itm in items1:
                curV = itm[0]
                curW = itm[1]
                addedValue = False
                for itm2 in items2:
                    if itm2[0] == curV:
                        curW += itm2[1]
                        ans.append([curV, curW])
                        addedValue = True
                        break
                if (addedValue == False):
                    ans.append([curV, curW])    

                    
        else:
            for itm in items2:
                curV = itm[0]
                curW = itm[1]
                addedValue = False
                for itm2 in items1:
                    if itm2[0] == curV:
                        curW += itm2[1]
                        ans.append([curV, curW])
                        addedValue = True
                        break
                    
                if (addedValue == False):
                    ans.append([curV, curW]) 
        ans = sorted(ans, key =lambda x: x[0])
            
        return ans
    
items1 = [[1,1],[4,5],[3,8]]
items2 = [[3,1],[1,5]]

answer = Solution.mergeSimilarItems(items1, items2)
print(answer)

        