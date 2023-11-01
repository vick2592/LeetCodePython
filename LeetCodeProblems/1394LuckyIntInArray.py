class Solution:
    def findLucky(arr):
        track = {}
        for n in arr:
            track[n] = 0
        for n in arr:
            track[n] += 1;
        lucky_numbers = 0
        for k in track.keys():
            if k == track[k]:
                lucky_numbers += 1

        if lucky_numbers == 0:
            return -1
        else: 
            return lucky_numbers

arr = [1,2,2,3,3,3]
answer = Solution.findLucky(arr)
print(answer)