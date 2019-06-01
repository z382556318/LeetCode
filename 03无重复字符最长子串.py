class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0: return 0
        max_length = 1
        l = len(s)
        for i in range(l):
            long = 1
            data = set(s[i])
            for j in range(i+1,l):
                if s[j] not in data:
                    data.add(s[j])
                    long += 1
                else:
                    if long > max_length:
                        max_length = long
                    break
            # 整个字符串均不同，需最后比较一次
            if long > max_length:
                max_length = long
        return max_length


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0: return 0
        left = 0
        max_len = 0
        cur_len = 0
        new_str = set()
        for i in range(len(s)):
            cur_len += 1
            while s[i] in new_str:
                new_str.remove(s[left])
                left += 1
                cur_len -= 1
            if cur_len > max_len: max_len = cur_len
            new_str.add(s[i])
        return max_len

if __name__ == '__main__':
    s = 'a'
    print(Solution().lengthOfLongestSubstring(s))