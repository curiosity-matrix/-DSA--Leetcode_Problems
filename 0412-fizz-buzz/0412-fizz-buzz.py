class Solution(object):
    def fizzBuzz(self, n):
        l=[]
        """
        :type n: int
        :rtype: List[str]
        """
        for i in range(1,n+1):
            if i%15==0:
                l.append("FizzBuzz")
            elif (i%3==0):
                l.append("Fizz")
            elif (i%5==0):
                l.append("Buzz")
            else:
                l.append(str(i))


        return l

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna