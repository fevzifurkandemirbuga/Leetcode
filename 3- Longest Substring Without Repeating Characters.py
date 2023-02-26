class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
    
        String=str()
        result=int()
        for i in s:
            if i in String:
                String=String[String.find(i)+1::]
            String=String+i
            if len(String)>result:
                result=len(String)
        return result