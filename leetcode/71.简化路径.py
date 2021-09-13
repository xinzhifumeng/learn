#
# @lc app=leetcode.cn id=71 lang=python3
#
# [71] 简化路径
#类似linux路径
#栈控制路径

# @lc code=start
class Solution:
    def simplifyPath(self, path: str) -> str:
        l=path.split('/')
        #利用/进行分割,开始的/ 以及// 会成为' '
        res,i=[],0
        while i<len(l):
            if l[i]=='..':
                if res:res.pop()
                #将路径顶出栈，得到上一个路径
            elif l[i]!='.' and l[i]!='':
                res.append(l[i])
                #路径入栈
            i+=1
        return '/'+'/'.join(res)
        #开头和列表中间加入/


'''
首先根据'/'将path进行split，用res保存简化后需要的文件名，对于每个元素进行分类讨论，

如果是 . 或者 空字符串 则跳过
如果是.. 说明需要返回上一级，即弹出一个文件名，但是这里有一个细节需要注意，只有res非空的时候才能弹出，否则对于测试用例 '/../'不能通过
如果是普通的文件名，则加入res
最后用'/'连接起来，并且在首部加上'/'即可

作者：yuer-flyfly
链接：https://leetcode-cn.com/problems/simplify-path/solution/jian-hua-lu-jing-jian-dan-yi-dong-yong-z-lytv/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''



# @lc code=end

