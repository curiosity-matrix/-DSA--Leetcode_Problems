class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        length=len(s)
        count=0
        for i in range(length-1,-1,-1):
            if s[i]==" " and count==0:
                continue
            elif s[i] != " ":
                count+=1
            else:
                break
        return count

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna