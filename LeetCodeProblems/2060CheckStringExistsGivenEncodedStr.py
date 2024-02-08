class Solution:
    def possiblyEquals(s1, s2):
        def generate_combinations(dictionary, index=0, current=''):
            # Base case: if we've added a character for each position, add the string to the list
            if index == len(dictionary):
                return [current]

            # Recursive case: for each possible string at this position, add it to the string and recurse
            result = []
            for string in dictionary[index]:
                if string.isdigit():
                    temp = '*' * int(string)
                else:
                    temp = string
                result += generate_combinations(dictionary, index + len(string), current + temp)
            return result
        decodeStr1 = []
        decodeStr2 = []

        for i in range(len(s1)):
            decodeStr1.append(s1[i])
            
        for j in range(len(s2)):
            decodeStr2.append(s2[j])
        
        dictMap = {}
        for x in range(len(decodeStr2)):
            if decodeStr2[x].isdigit():
                dictMap[x] = [decodeStr2[x]]
                y = x+1
                while(y < len(decodeStr2) and decodeStr2[y].isdigit()):
                    dictMap[x].append(decodeStr2[y])
                    y += 1
            else: 
                dictMap[x] = [decodeStr2[x]]
        
        #write me a loop to get all combinations in the dictMap 
        for k,v in dictMap.items():
            tempL = []
            tempS = ""
            for i in range(len(v)):
                tempS += v[i]
                tempL.append(tempS)
            dictMap[k] = tempL
            
        allCombs = generate_combinations(dictMap)
        
        dictMap1 = {}
        for x in range(len(decodeStr1)):
            if decodeStr1[x].isdigit():
                dictMap1[x] = [decodeStr1[x]]
                y = x+1
                while(y < len(decodeStr1) and decodeStr1[y].isdigit()):
                    dictMap1[x].append(decodeStr1[y])
                    y += 1
            else: 
                dictMap1[x] = [decodeStr1[x]]
        
        #write me a loop to get all combinations in the dictMap 
        for k,v in dictMap1.items():
            tempL = []
            tempS = ""
            for i in range(len(v)):
                tempS += v[i]
                tempL.append(tempS)
            dictMap1[k] = tempL
            
        allCombs1 = generate_combinations(dictMap1)
        found = False
        for d in allCombs:
            for e in allCombs1:
                if len(d) == len(e):
                    for f in range(len(d)):
                        if d[f] == e[f] or d[f] == '*':
                            if(f == len(d) - 1):
                                found = True
                            continue
                        else:
                            break
                        

        return found
    
s1 = "internationalization"
s2 = "i18n"
s1 = "l123e"
s2 = "44"
s1 = "a5b"
s2 = "c5b"
ans = Solution.possiblyEquals(s1, s2)
print(ans)
