class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """

        rev_bits =""
        while (n>0):
            
            rem=n%2
            rev_bits+=str(rem)
            n=n//2
        while len(rev_bits)<32:
            # need to insert 0 at last
            rev_bits+="0"
            # we got 32 bits in rev_bits
        p=len(rev_bits)-1
        ans=0
        for ele in rev_bits:
            ans+=int(ele)*2**p
            p-=1
        return ans
    
    
        
    
    
    
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna