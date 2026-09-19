class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d1={}
        d2={}
        if len(s)==len(t):

            for i in range(len(s)):  # or t

                if s[i] in d1:
                    if d1[s[i]]!=t[i]:
                        return(False)
                        break
            
                if t[i] in d2:
                    if d2[t[i]]!=s[i]:
                        return(False)
                        break


                d1[s[i]]=t[i]
                d2[t[i]]=s[i]                    
        
            return(True)

        else:
            return(False)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna