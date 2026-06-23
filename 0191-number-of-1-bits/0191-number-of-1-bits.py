class Solution:
    def hammingWeight(self, n: int) -> int:
        c=0
        while (n>0):
            if (n%2==1):
                c+=1
            n=n//2
        return c
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna