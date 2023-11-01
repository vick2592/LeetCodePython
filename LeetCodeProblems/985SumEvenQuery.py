class Solution:
    def sumEvenAfterQueries(nums, queries):
        answer = []
        maskNums = nums
        for i in queries:
            temp = []
            print("the ith array index is ", str(i[1]))
            print("the ith array value is ", str(i[0]))
            maskNums[i[1]] = maskNums[i[1]] + i[0]
            for j in maskNums:
                print("Now we look at the new nums array with each j being ", str(j))
                if (j%2==0):
                    temp.append(j)
            total = 0
            for k in temp:
                total += k
            #print(total)
            answer.append(total)
    

        return answer

nums = [1,2,3,4]
queries = [[1,0],[-3,1],[-4,0],[2,3]]

answer = Solution.sumEvenAfterQueries(nums, queries)
print(answer)