#
# @lc app=leetcode.cn id=82 lang=python3
#
# [82] 删除排序链表中的重复元素 II
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head: return head 

        dummy=ListNode(0,head)

        cur=dummy
        while cur.next and cur.next.next:
            if cur.next.val == cur.next.next.val:
                x = cur.next.val
                while cur.next and cur.next.val == x :
                    #此处记下x的值，方便删除多个值，而不是只删除两个
                    cur.next = cur.next.next
            else:
                cur=cur.next
            
        return dummy.next
# @lc code=end

