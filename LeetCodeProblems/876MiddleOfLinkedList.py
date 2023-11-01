import math

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(head):
        if(len(head) % 2 == 0):
            middle = math.ceil(len(head) / 2)
        else:
            middle = math.ceil(len(head) / 2) - 1

        print(middle)

        ansList = head[middle:]

        return ansList
head = [1,2,3,4,5,6]

answer = Solution.middleNode(head)
print(answer)