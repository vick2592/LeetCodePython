class Solution:
    def closestRoom(rooms, queries):
        answer = []
        for x in range(len(queries)):
            minRoom = [-1, -1]
            for y in range(len(rooms)):
                if queries[x][1] > rooms[y][1]:
                    continue
                else:
                    absDiff = abs(queries[x][0] - rooms[y][0])
                    if absDiff < minRoom[1] or minRoom[1] == -1:
                        minRoom = [rooms[y][0], absDiff]
                    elif absDiff == minRoom[1]:
                        if rooms[y][0] < minRoom[0]:
                            minRoom = [rooms[y][0], absDiff]

            answer.append(minRoom[0])

        return answer

rooms = [[2,2],[1,2],[3,2]]
queries = [[3,1],[3,3],[5,2]]

rooms = [[1,4],[2,3],[3,5],[4,1],[5,2]]
queries = [[2,3],[2,4],[2,5]]

answer = Solution.closestRoom(rooms, queries)
print(answer)  # Expected output: [1,2,3]
