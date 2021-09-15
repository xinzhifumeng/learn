#
# @lc app=leetcode.cn id=89 lang=python3
#
# [89] 格雷编码
#类似遍历二进制

# @lc code=start
class Solution:
    def grayCode(self, n: int) -> List[int]:
        res,head=[0],1
        for i in range(n):
            for j in range(len(res)-1,-1,-1):
                 res.append(head+res[j])
            head <<=1 
            #有找规律的嫌疑，利用对head的进位，分别加0和1最后输出结果
            # head =head *(2**1)  <<代表2的进位操作,反之则退位
        return res

# @lc code=end

