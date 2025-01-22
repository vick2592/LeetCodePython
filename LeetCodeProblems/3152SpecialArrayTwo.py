class Solution:
    def isArraySpecial(nums, queries):
        answer = []
        for q in queries:
            isOdd = nums[q[0]] % 2 == 1
            special = True
            for i in range(q[0] + 1, q[1] + 1):
                if (isOdd and nums[i] % 2 == 1) or (not isOdd and nums[i] % 2 == 0):
                    special = False
                    break
                isOdd = not isOdd
            answer.append(special)
        return answer

nums = [4,3,1,6]
queries = [[0,2],[2,3]]

answer = Solution.isArraySpecial(nums, queries)
print(answer)