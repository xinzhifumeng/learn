#
# @lc app=leetcode.cn id=43 lang=python3
#
# [43] 字符串相乘
#

# @lc code=start
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if (num1=="0" or num2=="0"):return "0"

       
        res=[0]*(len(num1)+len(num2))

        for i in range(len(num1)-1, -1, -1):
            for j in range(len(num2)-1, -1, -1):

                temp=int(num2[j])*int(num1[i])
                p1=i+j
                p2=i+j+1
                sum=temp+res[p2]
                res[p2]=sum%10
                res[p1]+=sum//10
                j-=1
            i-=1
        for i in range(len(res)):    # 去除res前面的0
            if res[i] != 0:
                break
        res = [str(v) for v in res[i:]]

        return "".join(res)




      
# @lc code=end

