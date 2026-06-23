class Solution(object):
    def isPalindrome(self, x):
        orig=x
        rev=0
        while x>0:
            rem=x%10
            rev=rev*10+rem
            x=x//10
        return orig==rev
            

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna