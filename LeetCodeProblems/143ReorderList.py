# Definition for singly-linked list.
#class ListNode:
#    def __init__(self, val=0, next=None):
#        self.val = val
#        self.next = next


class Solution:
    def reorderList(head):
        forwardCount = 0
        reverseCount = -1
        listSize = len(head)
        headCopy = head.copy()
        for i in range(0,listSize):
            if i % 2 == 0:
                head[i] = headCopy[forwardCount]
                forwardCount += 1

            if i % 2 == 1:
                head[i] = headCopy[reverseCount]
                reverseCount -= 1

        """
        Do not return anything, modify head in-place instead.
        """

head = [1,2,3,4]

print("Head before update: ", head)
Solution.reorderList(head)
print("Head after update: ", head)