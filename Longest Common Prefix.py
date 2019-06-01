class Solution1:
    def longestCommonPrefix(self,strs):
        a = ''
        i = 0
        while (strs[0][i] and strs[1][i] and strs[2][i]):               # 需要修正
            if strs[0][i] == strs[1][i] and strs[0][i] == strs[2][i]:
                i += 1
            else:
                break

        return strs[0][0:i]                         # 冒号 ，与range（0，1）不同

class Solution2:
    def longestCommonPrefix(self,strs) -> str:
        if len(strs) == 0: return ''
        prefix = strs[0]
        for i in range(0,len(strs)):
            while (strs[i].find(prefix) != 0):
                prefix = prefix[0:len(prefix) - 1]
                if (len(prefix) == 0): return ""
        return prefix

class Solution3:
    def longestCommonPrefix(self,strs):
        if len(strs) == 0: return ''
        for j in range(0,len(strs[0])):
            common_ch = strs[0][j]
            for i in range(0,len(strs)):
                if (common_ch != strs[i][j]) or (len(strs[i]) == j):
                    return strs[0][0:j]
                else:continue
        return strs[0]

class Solution4:
    # 分治
    def longestCommonPrefix(self, strs):
        if len(strs) == 0: return ''

class Solution5:
    # 二分查找法
    def

class Solution6:
    # 字典树
    def



x = []
solution = Solution3()
a = solution.longestCommonPrefix(x)
print(a)
