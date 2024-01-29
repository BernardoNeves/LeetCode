class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        p = {")": "(", "]": "[", "}": "{"}

        stack = []
        for c in s:
            if c in p and stack:
                if stack[-1] != p[c]:
                    return False
                stack.pop()
            else:
                stack.append(c)
        return not stack
