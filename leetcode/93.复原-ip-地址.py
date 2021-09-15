#
# @lc app=leetcode.cn id=93 lang=python3
#
# [93] 复原 IP 地址
#分成4断
#每段小于256，且开头不为零

# @lc code=start
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        """
            一共四位，每一位都可以取 0 - 255之间这些数字，也就是，每一位都可以取 1 - 3位，也就是每一位都有三种取法。
            抽象出来就是四层，三叉树。
            从中去掉不符合规则的就可以了。
        """
        if len(s) < 4: return []
        
        rst = []
        def getIP(IP: list, idx):
            # 4. 长度大于 4 剪枝 
            if len(IP) == 4:
                # 5. 正好取完，才对
                if idx == len(s):
                    rst.append('.'.join(IP))
                return 
                
            for i in range(1, 4):
                # 3. 这个可加可不加，是因为 假如 'ab' 切片长度大于 2，都是 取ab，那么会取到两个相同结果，
                # 但是5会限制，只有idx == len(s) 才会取 
                if idx + i > len(s):
                    continue
                sub = s[idx: idx + i]
                # 1. 包含前导0， 剪枝
                if len(sub) > 1 and sub[0] == '0':
                    continue
                # 2. 当取得这一位大于255，直接剪枝
                if int(sub) > 255:
                    continue
                IP.append(sub)
                getIP(IP, idx + i)
                IP.pop()
            
        getIP([], 0)
        return rst

# @lc code=end

