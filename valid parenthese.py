class Solution1:
    def isValid(self,s:str) -> bool:
        mapping = {
            ')':'(',
            '}':'{',
            ']':'['
        }
        stack = []
        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else '#'
                # 相当于
                # top_element = (stack.pop(-1) if stack else '#')
                # a = [1,2,3]
                # b = a if len(a) != 0 else ""
                # print(b)
                # 输出：[1,2,3]
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)
        return not stack

x = '{[()]}'
solution = Solution1()
a = solution.isValid(x)
print(a)