#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        

        #迭代法
        dummyHead = ListNode(0)
        dummyHead.next = head
        temp = dummyHead
        while temp.next and temp.next.next:
            node1 = temp.next
            node2 = temp.next.next
            temp.next = node2
            node1.next = node2.next
            node2.next = node1
            temp = node1
        return dummyHead.next

        '''
        #堆栈解题，一次放两个节点
		if not (head and head.next):
			return head
		p = ListNode(-1)
		# 用stack保存每次迭代的两个节点
		# head指向新的p节点，函数结束时返回head.next即可
		cur,head,stack = head,p,[]
		while cur and cur.next:
			# 将两个节点放入stack中
			_,_ = stack.append(cur),stack.append(cur.next)
			# 当前节点往前走两步
			cur = cur.next.next
			# 从stack中弹出两个节点，然后用p节点指向新弹出的两个节点
			p.next = stack.pop()
			p.next.next = stack.pop()
			p = p.next.next
		# 注意边界条件，当链表长度是奇数时，cur就不为空	
		if cur:
			p.next = cur
		else:
			p.next = None
		return head.next

        #https://leetcode-cn.com/problems/swap-nodes-in-pairs/solution/dong-hua-yan-shi-24-liang-liang-jiao-huan-lian-bia/
        '''



        '''
        #递归的方法-来自官方
        #带入1234 理解一下就行了 1-234 第一步后求34返回第一步43后执行完2143
        if not head or not head.next: return head 
        newhead=head.next
        head.next=self.swapPairs(newhead.next)
        newhead.next=head
        return newhead
        '''
# @lc code=end

