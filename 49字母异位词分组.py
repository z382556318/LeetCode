# class Solution:
#     def groupAnagrams(self, strs):
#         if not strs:
#             return []
#
#         info = {}
#         for s in strs:
#             tmp = []
#             for c in s:
#                 tmp.append(c)
#             tmp = tuple(tmp)
#             # 不可改变，但有顺序
#             if tmp not in info.keys():
#                 info[tmp] = [s]
#             else:
#                 info[tmp].append(s)
#
#         return list(info.values())
#
# print(list(Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"])))
class Solution:
    def groupAnagrams(self, strs):
        if not strs:
            return []

        info = {}
        for s in strs:
            if tuple(sorted(s)) not in info.keys():
                info[tuple(sorted(s))] = [s]
            else:
                info[tuple(sorted(s))].append(s)
        return list(info.values())

print(list(Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"])))
import collections

class Solution(object):
    def groupAnagrams(self, strs):
        ans = collections.defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return ans.values()