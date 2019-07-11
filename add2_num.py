# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2, memory = 0):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        start_node = ListNode(0)
        tmp_node = start_node # Instantiate a new temp node
        while(l1 or l2 or memory):
            l1 = (l1 if l1 else ListNode(0))
            l2 = (l2 if l2 else ListNode(0))
            sum = l1.val + l2.val + memory
            if (sum > 9):
                memory = 1
                sum -= 10
            else:
                memory = 0
                
            l1 = l1.next
            l2 = l2.next
            new_node = ListNode(sum)
            tmp_node.next = new_node
            tmp_node = tmp_node.next
            
        return start_node.next
        
