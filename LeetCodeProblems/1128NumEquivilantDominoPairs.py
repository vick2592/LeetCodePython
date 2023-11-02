class Solution:
    def numEquivDominoPairs(dominoes):
        count = 0
        for x in range(len(dominoes)):
            for y in range(x+1, len(dominoes)):
                if dominoes[x][0] == dominoes[y][0] and dominoes[x][1] == dominoes[y][1]:
                    count += 1
                elif dominoes[x][0] == dominoes[y][1] and dominoes[x][1] == dominoes[y][0]:
                    count += 1
                else:
                    continue
        return count
    
dominoes = [[1,2],[1,2],[1,1],[1,2],[2,2]]
answer = Solution.numEquivDominoPairs(dominoes)

print(answer)