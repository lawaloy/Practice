# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        if not head:
            return head
        curSum = 0
        unOrderedMap = {}
        unOrderedMap[0] = dummyNode = ListNode(0)
        dummyNode.next = currHead = head
        while currHead:
            curSum += currHead.val
            unOrderedMap[curSum] = currHead
            currHead = currHead.next
        
        currSum = 0
        currHead = dummyNode
        while currHead:
            currSum += currHead.val
            currHead.next = unOrderedMap[currSum].next
            currHead = currHead.next
        return dummyNode.next
