class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = {}
        for s in strs:
            key = "".join(sorted(s))
            dic.setdefault(key, []).append(s)
        return list(dic.values())
