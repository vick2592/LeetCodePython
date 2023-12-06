class Solution:
    def minOperations(boxes):
        answer = []
        for i in range(len(boxes)):
            count = 0
            for j in range(len(boxes)):
                if i != j and boxes[j] == "1":
                    count += abs(i-j)
            answer.append(count)
        return answer
        
boxes = "001011"
answer = Solution.minOperations(boxes)
print(answer)