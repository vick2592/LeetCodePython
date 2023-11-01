from csv import QUOTE_ALL
from heapq import heappop, heappush
import math


class Solution:
    def mincostToHireWorkers(quality, wage, k):
        workers = [(w/q, q) for q, w in zip(quality, wage)]
        workers.sort()  # sort in increasing order by ratio
        #print(workers)
        maxHeap = []
        totalQuality = 0
        minCost = math.inf
        for r, q in workers:
            heappush(maxHeap, -q)
            totalQuality += q
            if len(maxHeap) > k:
                totalQuality += heappop(maxHeap)
            if len(maxHeap) == k:
                minCost = min(minCost, totalQuality * r)
        return minCost

quality = [3,1,10,10,1]
wage = [4,8,2,2,7]
k = 3

print(Solution.mincostToHireWorkers(quality, wage, k))

print("Hello world!")