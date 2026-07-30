class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        """
        return sorted(s)==sorted(t)
        """
        arr1=[0]*26
        arr2=[0]*26
        for ch1 in s:
            idx1=ord(ch1)-ord('a')
            arr1[idx1]+=1
        for ch2 in t:
            idx2=ord(ch2)-ord('a')
            arr2[idx2]+=1
        return arr1==arr2
            
        return arr1==arr2


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna