# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        x=1
        sum1=0
        sum2=0
        while l1!=None or l2!=None:
            if l1!=None :
                sum1+=l1.val*x
                l1=l1.next
            if l2!=None:
                sum2+=l2.val*x
                l2=l2.next
            x*=10
       

        result=str(sum1+sum2)
        temp=None
        for i in result:
            answer=ListNode(int(i),temp)
            temp=answer
        return answer




        