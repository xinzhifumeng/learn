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

    #双指针方法
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)#head添加哑节点
        first = head
        second = dummy
        for i in range(n):
            first = first.next
            #将fist遍历到n的位置，fist比second领先了n个位置

        while first:
            first = first.next
            second = second.next
            #在first上继续遍历，直到firs为空，此时second的位置就是倒数n的位置
        
        second.next = second.next.next
        return dummy.next




'''
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        #栈
        dummy = ListNode(0, head)
        stack = list()
        cur = dummy
        while cur:#全部入栈
            stack.append(cur)
            cur = cur.next
        
        for i in range(n):#弹出栈直到第n个
            stack.pop()

        prev = stack[-1]
        prev.next = prev.next.next
        #栈内剩下的就是需要去除的head节点
        return dummy.next
'''
'''
#官方解法，计算链表长度
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        def getLength(head : ListNode)->int:
            length=0
            while head:
                #利用循环遍历链表得到链表长度
                length+=1
                head =head.next
            return length
        
        dummy=ListNode(0,head)#head前面加上哑节点
        length=getLength(head)
        cur=dummy
        for i in range(1,length-n+1):
            cur=cur.next  #进位
        cur.next=cur.next.next 
        #执行删除操作，cur的操作影响到了dummy
        return dummy.next
'''



# @lc code=end

