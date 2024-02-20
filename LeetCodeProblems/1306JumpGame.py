
# My Solution
# class Solution:
#     def canReach(arr, start):
#         for i in range(len(arr)):
#             if i == start or start + arr[i] == start or start - arr[i] == start:
#                 continue
#             if start + arr[i] < len(arr) and arr[start + arr[i]] == 0:
#                 return True
#             if start - arr[i] >= 0 and arr[start - arr[i]] == 0:
#                 return True
            
#         return False

#Copilots Solution
class Solution:
    def canReach(self, arr, start):
        visited = [False] * len(arr)

        def dfs(index):
            if index < 0 or index >= len(arr) or visited[index]:
                return False
            if arr[index] == 0:
                return True

            visited[index] = True

            # try to jump forward and backward
            return dfs(index + arr[index]) or dfs(index - arr[index])

        return dfs(start)
arr = [4,2,3,0,3,1,2]
start = 5
arr = [3,0,2,1,2]
start = 2

ans = Solution()

print(ans.canReach(arr, start))