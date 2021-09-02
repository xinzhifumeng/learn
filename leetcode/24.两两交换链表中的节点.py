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
        #定义一哑节点
        dummyHead.next = head
        #链接到链表最前面
        temp = dummyHead
        #定义临时节点放在开头，循环中表示上一个循环末尾的节点，并控制循环进行

        while temp.next and temp.next.next:
            #同时存在两个节点
            node1 = temp.next
            node2 = temp.next.next
            #对本次循环中的node1 node2 赋值
            temp.next = node2 #链接上一个循环结果，第一次链接的哑节点
            node1.next = node2.next
            node2.next = node1
            #转移链接，实现互换
            temp = node1
            #交换完后通过temp进位，在下个循环中进行下两位
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
        #末尾是否存在，或只存在1项
        newhead=head.next
        #第二项提到前面
        head.next=self.swapPairs(newhead.next)
        #将两项后的项连接到第一项后面，加上迭代运算看一看做已完成的项
        newhead.next=head
        #将第一项连接到新链表的第二项后
        return newhead
        '''
# @lc code=end

