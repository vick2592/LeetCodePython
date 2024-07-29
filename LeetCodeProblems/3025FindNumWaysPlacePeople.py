class Solution:
    def numberOfPairs(points):
        #Sort by the highest y axies and smallest x axies
        points.sort(key=lambda x: (-x[1], x[0]))
        print(points)
        count = 0
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                testSq = [points[i], points[j]]
                print(testSq)
                if testSq[0][1] >= testSq[1][1]:
                    noGood = False
                    for k in range(len(points)):
                        if k == i or k == j:
                            continue
                        else:
                            if points[k][0] >= testSq[0][0] and points[k][0] <= testSq[1][0] and points[k][1] <= testSq[0][1] and points[k][1] >= testSq[1][1]:
                                noGood = True
                                break
                    if noGood == False:
                        count += 1
                    
        return count
    
points = [[6,2],[4,4],[2,6]]
# points = [[3,1],[1,3],[1,1]]
answer = Solution.numberOfPairs(points)
print(answer)  # Expected output: 1
