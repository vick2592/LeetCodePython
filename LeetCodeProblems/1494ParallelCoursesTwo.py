class Solution:
    def minNumberOfSemesters(n, relations, k):
        cDict = {}
        courses = [x for x in range(1, n+1)]
        for c in courses:
            cDict[c] = 0
        for c in relations:
            cDict[c[1]] += 1
        print(cDict)
        print(courses)

        fullDict = {}
        for cd in list(cDict.items()):
            if cd[1] not in fullDict:
                fullDict[cd[1]] = 1
            else:
                fullDict[cd[1]] += 1
                
        print("Full Dict is: ", fullDict)
        count = 0
        for c in fullDict:
            remainder = fullDict[c]
            # print(remainder)
            while remainder > 0:
                remainder -= k
                count += 1  
        
        return count;

n = 5
relations = [[2,1],[3,1],[4,1],[1,5]]
k = 3

answer = Solution.minNumberOfSemesters(n, relations, k)
print(answer)