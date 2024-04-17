class Solution:
    def minimumScore(s, t):
        
        enumT = list(enumerate(t))
        print(enumT)
        def getTsubs(enumT):
            if len(enumT) == 0:
                return [(set(), "")]
            else:
                first = enumT[0]
                rest = enumT[1:]
                subs_without_first = getTsubs(rest)
                subs_with_first = [(sub[0].union({first[0]}), first[1] + sub[1]) for sub in subs_without_first]
                return subs_without_first + subs_with_first

        allTsubs = getTsubs(enumT)
        print(allTsubs)
        
        def get_subsequences(s):
            if s == "":
                return [""]
            else:
                first = s[0]
                rest = s[1:]
                subs = get_subsequences(rest)
                return subs + [first + sub for sub in subs]
                
        allSubStr = get_subsequences(s)
        score = 10000000000
        print(allSubStr)
        for ts in allTsubs:
            if ts[1] in allSubStr:
                testL = 0
                testS = 10000000000
                for n in range(len(t)):
                    if n not in ts[0]:
                        if testS > n:
                            testS = n
                        if testL < n:
                            testL = n
                if testS == 10000000000:
                    continue
                if score > testL - testS + 1:
                    score = testL - testS + 1
                    
        if score < 10000000000:
            return score
                           
        return 0
s = "abacaba"
t = "bzaa"
# s = "cde"
# t = "xyz"
print(Solution.minimumScore(s, t))