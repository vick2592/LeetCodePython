class Solution:
    def complexNumberMultiply(num1, num2):
        r1 = int(num1.split("+")[0])
        r2 = int(num2.split("+")[0])
        i1 = int(num1.split("+")[1].split("i")[0])
        i2 = int(num2.split("+")[1].split("i")[0])
        if (num1.split("+")[1].split("i")[1]) == '': 
            i1exp = 1
        else:
            i1exp = int(num1.split("+")[1].split("i")[1])
        if (num2.split("+")[1].split("i")[1]) == '':
            i2exp = 1
        else:
            i2exp = int(num2.split("+")[1].split("i")[1])
        
        print(r1,r2,i1, i2)
        r1r2prod = (r1 * r2)
        r1i2prod = (r1 * i2)
        i1r2prod = (i1 * r2)
        i1i2prod = (i1 * i2)
        ili2prodExp = (i1exp+i2exp)
        tempExp = ili2prodExp
        iExp = 1
        remainderIexp = 0        

        while tempExp >= 2:
            tempExp -= 2
            iExp *= -1
            if tempExp == 1:
                remainderIexp = 1
                
        if remainderIexp == 1:
            i1PLUSi2 = str(i1i2prod + r1i2prod + i1r2prod) + 'i'
        else:
            i1PLUSi2 = ''
        
        r1i2PLUSi1r2 = str(r1i2prod + i1r2prod) + 'i'
        if iExp != 1:
            r1PLUSr2 = str(r1r2prod + iExp)
        else:
            r1PLUSr2 = str(r1r2prod)
        
        if i1PLUSi2 != '':
            ans = r1PLUSr2 + '+' + i1PLUSi2
        else:
            ans = r1PLUSr2 + '+' + r1i2PLUSi1r2
            
        return ans
num1 = "1+-1i"
num2 = "1+-1i"

num1 = "1+1i"
num2 = "1+1i"

answer = Solution.complexNumberMultiply(num1, num2)
print(answer)

