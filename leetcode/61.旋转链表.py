#
# @lc app=leetcode.cn id=61 lang=python3
#
# [61] 旋转链表
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 0 or not head or not head.next:return head 

        n = 1
        cur = head #cur理解为指针的话，拼合成一个循环链就好理解了
        while cur.next:
            cur = cur.next
            n += 1
        
        if (add := n - k % n) == n:return head 

        cur.next=head #有了之前的遍历，此处形成了循环
        while add:
            cur = cur.next 
            add -= 1
        ret = cur.next 
        cur.next = None #断链
        return ret

# @lc code=end

