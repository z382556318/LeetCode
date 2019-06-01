class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if not s or not numRows: return ""
        if numRows == 1 or numRows >= len(s): return s

        l = len(s)
        new_str = ""
        interval = 2 * (numRows-1)
        for start in range(numRows):
            new_str += s[start]
            tmp = start
            if start == 0 or start == numRows - 1:
                while tmp + interval < l:
                    tmp += interval
                    new_str += s[tmp]
            else:
                interval_1 = interval - start * 2
                while True:
                    if tmp + interval < l:
                        new_str += s[tmp + interval_1]
                        new_str += s[tmp + interval]
                        tmp += interval
                    elif tmp + interval_1 < l:
                        new_str += s[tmp + interval_1]
                        break
                    else:
                        break
        return new_str

if __name__ == '__main__':
    s = "L"
    numRows = 4
    print(Solution().convert(s,numRows))