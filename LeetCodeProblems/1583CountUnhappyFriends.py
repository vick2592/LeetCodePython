class Solution:
    def unhappyFriends(n, preferences, pairs):
        count = 0
        def isUnhappy(preferences, x, y, u, v):
            if preferences[x].index(u) < preferences[x].index(y) and preferences[u].index(x) < preferences[u].index(v):
                return True
            if preferences[x].index(v) < preferences[x].index(y) and preferences[v].index(x) < preferences[v].index(u):
                return True
            return False
        for i in range(len(pairs)):
            for j in range(i+1, len(pairs)):
                if isUnhappy(preferences, pairs[i][0], pairs[i][1], pairs[j][0], pairs[j][1]):
                    count += 1
                if isUnhappy(preferences, pairs[i][1], pairs[i][0], pairs[j][1], pairs[j][0]):
                    count += 1
                if isUnhappy(preferences, pairs[i][0], pairs[i][1], pairs[j][1], pairs[j][0]):
                    count += 1
                if isUnhappy(preferences, pairs[i][1], pairs[i][0], pairs[j][0], pairs[j][1]):
                    count += 1
        return count
   
n = 4
preferences = [[1, 3, 2], [2, 3, 0], [1, 3, 0], [0, 2, 1]]
pairs = [[1, 3], [0, 2]]


n = 4
preferences = [[1, 2, 3], [3, 2, 0], [3, 1, 0], [1, 2, 0]]
pairs = [[0, 1], [2, 3]]

answer = Solution.unhappyFriends(n, preferences, pairs)
print(answer)


