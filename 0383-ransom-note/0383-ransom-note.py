class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        d1={}
        for ch in ransomNote:
            d1[ch]=d1.get(ch,0)+1
        d2={}
        for ch in magazine:
            d2[ch]=d2.get(ch,0)+1
        for ch in d1:
            if ch not in d2 or d1[ch]>d2[ch]:
                return False
        
        return True
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna