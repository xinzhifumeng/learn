#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1: return l2  # 终止条件，直到两个链表都空
        if not l2: return l1
        
        if l1.val <= l2.val:  # 递归调用
            l1.next = self.mergeTwoLists(l1.next,l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1,l2.next)
            return l2
'''
merge(1,1): 1->4->5->null, 1->2->3->6->null
    merge(2,2): 4->5->null, 1->2->3->6->null
    	merge(3,2): 4->5->null, 2->3->6->null
    		merge(4,2): 4->5->null, 3->6->null
    			merge(5,1): 4->5->null, 6->null
    				merge(6,1): 5->null, 6->null
    					merge(7): null, 6->null
    					return l2
    				l1.next --- 5->6->null, return l1
    			l1.next --- 4->5->6->null, return l1
    		l2.next --- 3->4->5->6->null, return l2
    	l2.next --- 2->3->4->5->6->null, return l2
    l2.next --- 1->2->3->4->5->6->null, return l2
l1.next --- 1->1->2->3->4->5->6->null, return l1
'''

# @lc code=end

