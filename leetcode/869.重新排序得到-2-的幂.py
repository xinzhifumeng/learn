#
# @lc app=leetcode.cn id=869 lang=python3
#
# [869] 重新排序得到 2 的幂
#medium
'''
给定正整数 N ，我们按任何顺序（包括原始顺序）将数字重新排序，注意其前导数字不能为零。

如果我们可以通过上述方式得到 2 的幂，返回 true；否则，返回 false。

 

示例 1：

输入：1
输出：true
示例 2：

输入：10
输出：false
示例 3：

输入：16
输出：true
示例 4：

输入：24
输出：false

示例 5：

输入：46
输出：true
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reordered-power-of-2
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
# @lc code=start
class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:  
        
        nums = sorted(list(str(n)))
        l = len(nums) 

        #回溯法从新排序，参考47
        res=[]
        def backtrack(nums, ans):
            
            if len(nums)==0 and len(str(ans)) == l:
                while ans>= 1:#幂的判定
                    if ans == 1 : 
                        res.append(ans)
                    if ans % 2 != 0 : break
                    ans = ans // 2 
                    
                return
            for i in range(len(nums)):
                if ans == 0 and nums[i] == 0 :continue
                #跳过0开头的组合
                if i >= 1 and nums[i] == nums[i-1]:continue
                backtrack(nums[:i]+nums[i+1:], ans * 10 + int(nums[i]))

        backtrack(nums, 0) 
       
        if not res : return False
        else : return True
        
 

# @lc code=end

