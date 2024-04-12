from copy import deepcopy

class Solution:
    def gcdSort(nums):
        masterList = [nums]
        def GCD(a, b):
            while (b != 0):
                temp = b;
                b = a % b;
                a = temp;
            return abs(a);
        def isSorted(arr):
            for i in range(len(arr)-1):
                if arr[i] > arr[i+1]:
                    return False
            return True
        queue = [nums]
        while (len(queue) > 0):
            test = deepcopy(queue.pop(0))
            print("test: ",test)
            if isSorted(test):
                return True
            for i in range(len(test)):
                for j in range(i+1, len(test)):
                    if GCD(test[i], test[j]) > 1:
                        test[i], test[j] = test[j], test[i]
                        if test not in masterList:
                            queue.append(deepcopy(test))
                            masterList.append(deepcopy(test))
        return False
    
nums = [7,21,3]
nums = [5,2,6,2]
nums = [10,5,9,3,15]
print(Solution.gcdSort(nums)) #1
        