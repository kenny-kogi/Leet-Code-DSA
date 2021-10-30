# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""




"""
Search a Linkded List in Python
"""


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
        ll1 = []
        ll2 = []
        while l1:
            ll1.append(l1.val)
            l1 = l1.next
        while l2:
            ll2.append(l2.val)
            l2 = l2.next
        s1 = ''
        s2 = ''
        for i in ll1:
            s1+=str(i)
        for i in ll2:
            s2+=str(i)
        num = int(s1[::-1])+int(s2[::-1])
        res = []
        for i in str(num)[::-1]:
            res.append(int(i))
        curr = dummy = ListNode(0)
        for i in res:
            curr.next = ListNode(i)
            curr = curr.next
        return dummy.next