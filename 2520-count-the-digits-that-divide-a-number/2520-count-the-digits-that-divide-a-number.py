class Solution(object):
    def countDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        
        # base case -> num>0
        # task1 -> dig extract
        # task2 -> div check
        # task 3 -> count

        c=0
        orig=num
        while num>0:
            lst_dig=num%10
            if orig%lst_dig==0:
                c+=1
            num=num//10
        return c

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna