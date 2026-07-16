class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        # base case - n>0
        # task1 -> extraction
        # task2 - prod
        # task3 - sum
        # task4 - compare

        prod=1
        sum=0
        while n>0:
            lst_dig=n%10
            prod=prod*lst_dig
            sum=sum+lst_dig
            n=n//10
        return (prod-sum)


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna