#
# @lc app=leetcode.cn id=83 lang=python3
#
# [83] 删除排序链表中的重复元素
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:return head
        cur=head
        while cur.next:
            if cur.val==cur.next.val:
                cur.next=cur.next.next 
            else:
                cur=cur.next
        return head
            


'''a针对list的解法，此处是listnode
        if not head: return head
        i=1
        temp=0
        while i<len(head):
            if  head[i]!=head[i-1]:
                head[temp]=head[i]
                temp+=1
            i+=1
        return head[0:temp]
'''

# @lc code=end

