class Solution:
    def construct2DArray(original, m, n):
        if(m*n != len(original)):
            return []
        else:
            answer = []
            temp = []
            for x in range(len(original)):
                temp.append(original[x])
                if((x+1)%n == 0):
                    answer.append(temp)
                    temp = []
            return answer

original = [1,2,3,4]
m = 2
n = 2

answer = Solution.construct2DArray(original, m, n)

print(answer)