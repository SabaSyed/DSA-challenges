# Given a string s, find the length of the longest without duplicate characters.

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        left = 0
        long = []
        length = 0
        for right in range(len(s)):
            while s[right] in long:
                print(long)
                long.remove(s[left])
                left+=1
            
            long.append(s[right])
            if len(long) > length:
                length = len(long)
        return length
            

        
