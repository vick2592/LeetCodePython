class Solution:
    def canSeePersonsCount(heights):
        visibleList = []
        for i in range(len(heights)):
            tallest = 0
            count = 0
            if i == len(heights)-1:
                visibleList.append(0)
                break
            for j in range(i+1, len(heights)):
                #End Sequence
                if (j == len(heights)-1):
                    #End due to highest J blocking further heights
                    if (heights[j] > heights[i]):
                        count+=1
                        visibleList.append(count)
                        break
                    #In Between
                    if(heights[j] > tallest and heights[j] < heights[i]):
                        count +=1
                        visibleList.append(count)
                        break
                    break
                #End due to highest J blocking further heights
                if (heights[j] > heights[i]):
                    count+=1
                    visibleList.append(count)
                    break
                #In Between
                if(heights[j] > tallest and heights[j] < heights[i]):
                    tallest = heights[j]
                    count +=1
                    continue
        return visibleList
heights = [10,6,8,5,11,9]
answer = Solution.canSeePersonsCount(heights)
print(answer)