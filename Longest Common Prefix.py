# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

class Solution(object):

    def match(self, str1, str2):
        prefix = []
        for i in range(min(len(str1), len(str2))):
            if str1[i] == str2[i]:
                prefix.append(str1[i])
            else:
                break
        return ''.join(prefix)

    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        prefix = strs[0]
        for i in range(1, len(strs)):
            prefix = self.match(prefix, strs[i])
            if not prefix:
                return ""  # No common prefix
        return prefix
