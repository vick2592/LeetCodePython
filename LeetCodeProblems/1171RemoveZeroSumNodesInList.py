# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(head):
        
        indexTrim = []
        for b in range(len(head)):
            count = 0
            for c in range(b, len(head)):
                count += head[c]
                if count == 0:
                    indexTrim += [[i for i in range(b, c+1)]]
                    count = 0
        print(indexTrim)
        finished = False
        for k in indexTrim:
            j = 0
            for i in k:
                head.pop(i-j)
                j+= 1
            stillZero = False
            for julie in range(len(head)):
                testCount = 0
                for vaiman in range(julie, len(head)):
                    testCount = testCount + head[vaiman]
                    if testCount == 0:
                        stillZero = True
                        break
                if stillZero:
                    break
            if stillZero == False:
                break
        return head
    
head = [1,2,-3,3,1]
head = [1,2,3,-3,4]
ans = Solution.removeZeroSumSublists(head)
print(ans)  # Output: [3,1]
        