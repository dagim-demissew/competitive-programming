class Solution(object):
    def addSpaces(self, s, spaces):
        """
        :type s: str
        :type spaces: List[int]
        :rtype: str
        """
        spaces_set = set(spaces)
        result = []
        for i in range(len(s)):
            if i in spaces_set:
                result.append(" ")  
            result.append(s[i])  
        return "".join(result)  