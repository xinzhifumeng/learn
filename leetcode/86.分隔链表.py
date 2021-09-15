#
# @lc app=leetcode.cn id=86 lang=python3
#
# [86] 分隔链表
#模拟两个链表，一个large 一个small

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        
        dummy1,dummy2=ListNode(),ListNode()
        small,large,cur=dummy1,dummy2,head

        while cur:
            if cur.val < x:
                small.next = cur
                small = small.next
            else:#此处实际上是>=x 的项，这就保证了后面的顺序不会发生变化
                large.next = cur
                large = large.next
            cur=cur.next

        small.next,large.next = dummy2.next, None
        return dummy1.next


# @lc code=end

