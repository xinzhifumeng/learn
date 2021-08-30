#
# @lc app=leetcode.cn id=6 lang=python3
#
# [6] Z 字形变换
#
#找规律，每个位置都是有规律的
#每个峰和谷之间间隔2n-1 个位置n=i=numRows为行数
#在中间值每个循环会出现两个值，循环末与初两个值之间相差2i 

# @lc code=start
class Solution:
    
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2: return s
        res = ["" for _ in range(numRows)]
        i, flag = 0, -1
        for c in s:
            res[i] += c #直接在i的位置后加元素？
            if i == 0 or i == numRows - 1: flag = -flag
            i += flag
        return "".join(res)
        #此时res为一个有n个元素的list,
        #join加入空元素后按照顺序输出,空元素不显示

'''
        l=len(s)
        i=1 
        xunhuan=0
        res=''
        max=0
        if numRows<2:
            return s 
        while i<=numRows:
            xunhuan=0
            while i==1 and  i+xunhuan*(2*numRows-2)<=l: 
                res+=s[i+xunhuan*(2*numRows-2)-1]
                xunhuan+=1
                max=xunhuan

            xunhuan=0
            while i!=1 and i!=numRows and xunhuan<max+1:
                if 0<i+xunhuan*(2*numRows-2)<=l: 
                    res+=s[i+xunhuan*(2*numRows-2)-1]
                xunhuan+=1
                    
                if 0<(i+xunhuan*(2*numRows-2)-2*(i-1))<=l: 
                    res+=s[(i+xunhuan*(2*numRows-2)-2*(i-1)-1)]
                    
            xunhuan=0                 
            while i==numRows and i+xunhuan*(2*numRows-2)<=l: 
                res+=s[i+xunhuan*(2*numRows-2)-1]
                xunhuan+=1

            i+=1
        return res
'''        
# @lc code=end

