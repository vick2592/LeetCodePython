from copy import deepcopy

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(head):
        errorCorrection = 0
        countDict = {} 
        copyHead = deepcopy(head)
        for i in head:
            countDict[i] = 0
        for ind, n in list(enumerate(copyHead)):
            countDict[n] += 1
            if countDict[n] > 1:
                countDict[n] -= 1
                head.pop(ind - errorCorrection)
                errorCorrection += 1
        return head
head = [1,1,2,3,3]
answer = Solution.deleteDuplicates(head)
print(answer)