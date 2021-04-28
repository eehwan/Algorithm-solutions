# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    # def __str__(self):
    #     result = "ListNode ["
    #     current = self
    #     while current:
    #         if result != "ListNode [":
    #             result += ", "
    #         result += str(current.val)
    #         current = current.next
    #     return result + "]"
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        int1 = ""
        while l1:
            int1 += str(l1.val)
            l1 = l1.next
        int2 = ""

        while l2:
            int2 += str(l2.val)
            l2 = l2.next
        answer = None

        for x in list(str(int(int1[::-1]) + int(int2[::-1]))):
            answer = ListNode(x, answer)
        return answer
    