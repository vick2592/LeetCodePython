class Solution:
    def flipgame(fronts,backs):
        flippers = []
        notFlip = []
        for i in range(len(fronts)):
            if fronts[i] == backs[i]:
                notFlip.append(fronts[i])
        for i in range(len(fronts)):
            if fronts[i] == backs[i]:
                continue
            else:
                if(fronts[i] not in notFlip):
                    flippers.append(fronts[i])
                if(backs[i] not in notFlip):
                    flippers.append(backs[i])
        if len(flippers) != 0:
            ans = min(flippers)
            return ans
        return 0
    
fronts = [1,2,4,4,7]
backs = [1,3,4,1,3]

print(Solution.flipgame(fronts, backs)) #2