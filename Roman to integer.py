class Solution1:
    def romanToInt(self,x:str) -> int:
        symbol = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        sum = 0
        for i in range(0,len(x)):
            if i == (len(x) - 1) or symbol[x[i]] >= symbol[x[i+1]]:
                sum = sum + symbol[x[i]]
            else:
                sum = sum - symbol[x[i]]
        # for i in range(0,len(x)):
        #     if i == len(x) - 1:
        #         sum = sum + symbol[x[i]]
        #     elif symbol[x[i]] < symbol[x[i+1]]:
        #         sum = sum - symbol[x[i]]
        #     else:
        #         sum = sum + symbol[x[i]]
        return sum

x = 'III'
solution = Solution1()
a = solution.romanToInt(x)
print(a)
