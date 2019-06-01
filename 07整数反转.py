class Solution1:
    def reverse_int(self,x:int):
        if not x: return 0
        # 如何区分是错误还是0的反转

        s = str(x)
        sign = True if s[0] is "-" else False
        res = []
        for w in s:
            res.insert(w, 0)

        new_s = int("".join(res).lstrip("0"))

