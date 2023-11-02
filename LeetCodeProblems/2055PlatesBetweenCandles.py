class Solution:
    def platesBetweenCandles(s, queries):
        counts = []
        for q in queries:
            ss = s[q[0]:q[1]+1]
            # print(ss)
            count = 0
            tempCount = 0
            hit_candle = False
            for c in ss:
                if c == "*":
                    if hit_candle:
                        tempCount += 1
                    continue
                elif c == "|" and tempCount > 0:
                    count += tempCount
                    tempCount = 0
                    hit_candle = True
                    continue
                if c == "|":
                    hit_candle = not hit_candle
            counts.append(count)       
        return counts
    
s = "**|**|***|"
queries = [[2,5],[5,9]]
answer = Solution.platesBetweenCandles(s, queries)
print(answer)