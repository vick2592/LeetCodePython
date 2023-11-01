
class Solution:
    def answerQueries(nums, queries):
        nums = sorted(nums)
        #print(nums)
        answer = []
        numbers = list(enumerate(nums))
        end = numbers[-1][0]
        # print(end)
        for n in queries:
            sumation = 0
            subsequence = []
            for index, i in numbers:
                sumation += i
                if sumation <= n:
                    subsequence.append(i)
                    if index == end:
                        length = len(subsequence)
                        answer.append(length)
                        break
                    continue
                else:
                    length = len(subsequence)
                    answer.append(length)
                    break

        if len(answer) == 0:
            return [0]

        return answer

nums = [4,5,2,1]
queries = [3,10,21]

newList = Solution.answerQueries(nums, queries)

print(newList)