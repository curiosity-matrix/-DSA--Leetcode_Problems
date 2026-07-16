class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mn=min(nums)
        mx=max(nums)
        def gcd(mn,mx):
            while(mn>0 and mx>0):
                if mn>mx:
                    mn=mn%mx
                else:
                    mx=mx%mn
            if mn==0:
                return mx
            else:
                return mn
        return gcd(mn,mx)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna