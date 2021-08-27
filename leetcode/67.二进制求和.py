#
# @lc app=leetcode.cn id=67 lang=python3
#
# [67] 二进制求和
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        l=max(len(a),len(b))
        while len(a)!=len(b):
            if len(a)>len(b):b='0'+b
            if len(a)<len(b):a='0'+a
        i=-1
        jinwei=0
        tem=[]
        res=''
        while  i >= -l:
            tem.insert(i,(int(a[i])+int(b[i])+jinwei))
            jinwei=0
            if tem[i]==2 and i!=(-l):
                tem[i]=0
                jinwei=1
            elif tem[i]==3 and i!=(-l):
                tem[i]=1
                jinwei=1
            elif tem[i]==2 and i==(-l):
                tem[i]=0
                jinwei=0
                tem.insert(0,1)
                res=str(tem[0])+str(tem[i])+res
                break
            elif tem[i]==3 and i==(-l):
                tem[i]=1
                jinwei=0
                tem.insert(0,1)
                res=str(tem[0])+str(tem[i])+res
                break
            res=str(tem[i])+res
            i+=-1
        return res
# @lc code=end

