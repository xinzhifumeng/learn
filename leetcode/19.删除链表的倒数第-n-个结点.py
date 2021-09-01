#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第 N 个结点
#

# @lc code=start
#Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:

'''官方解法，实在是没看懂
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        def getLength(head : ListNode)->int:
            length=0
            while head:
                length+=1
                head =head.next
            return length
        
        dummy=ListNode(0,head)#添加头结点,??顺便定义dummy??
        length=getLength(head)
        cur=dummy
        for i in range(1,length-n+1):
            cur=cur.next  
        cur.next=cur.next.next #??这里暗示cur和dummuy是双向的，直接跳过了要删的n??
        return dummy.next??这里把0去掉了??
'''
# @lc code=end

