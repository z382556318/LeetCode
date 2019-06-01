class Solution1:
    # 字符串方法
    def isPalindrome(self,x:int):
        a = str(x)
        j = len(a) - 1
        for i in range(0,len(a)):
            if a[i] != a[j]:
                return False
            elif a[i] == a[j]:
                j -= 1
            elif i == j:
                break
        return True

class Solution2:
    # 缺少10以下回文判定
    # 循环过程冗余
    def isPalindrome(self,x:int):
        re = 0
        if x < 0:
            return False
        while (x != 0):
            a = x % 10
            x = x // 10
            re = re * 10 + a
            if x == re:
                return True
            elif re > x:
                if (x * 10 + a) == re:
                    return True
                else:
                    return False
            else:
                continue

class Solution3:
    def isPalindrome(self,x:int):
        re = 0
        if x < 0 or (x < 10 and x != 0):
            return False
        while (x > re):
            re = re * 10 + x % 10
            x = x // 10
        return re == x or re == x // 20

x = 421124
solution = Solution3()
a = solution.isPalindrome(x)
print(a)