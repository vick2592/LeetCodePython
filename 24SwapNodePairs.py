# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(head):
        for i in range(len(head)):
            if i % 2 == 1:
                temp = head[i]
                head[i] = head[i-1]
                head[i-1] = temp
        return head

head = [1,2,3,4]
answer = Solution.swapPairs(head)
print(answer)
nxt = ListNode()
rootNode = ListNode(head[0], nxt)
node = rootNode.next
#print("Current rootNode next value is: ", node.val)
for n in range(1, len(head)):
    if(n == len(head) - 1):
        node.val = head[n]
        break
    nxtN = ListNode()
    node.val = head[n]
    node.next = nxtN
    node = node.next
testNode = rootNode
while(True):
    if(testNode == None):
        break
    print("Current node val is: ", testNode.val)
    testNode = testNode.next