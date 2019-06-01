
class Solution:
    def __init__(self):
        self.data = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

    def func1(self, s):
        res = []
        if len(s) > 1:
            substrings = self.func1(s[1:])
            for c0 in self.data[s[0]]:
                for subs in substrings:
                    res.append(c0 + subs)
        else:
            for c1 in self.data[s[0]]:
                res.append(c1)
        return res

    def letterCombinations(self, digits: str):
        if not digits or not digits.isdigit():
            return []

        return self.func1(digits)

if __name__ == "__main__":
    print(Solution().letterCombinations("2"))