class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        def rev(s,l,r):
            if l>=r:
                return s

            s[l],s[r]=s[r],s[l]
            rev(s,l+1,r-1)


        rev(s,0,len(s)-1)   # 0,4

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna