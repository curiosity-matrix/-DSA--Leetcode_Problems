class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """

        arr=[0]*26
        for ch in s:
            idx=ord(ch)-ord('a')
            arr[idx]+=1
        for i,ele in enumerate(s):
            if arr[ord(ele)-ord('a')]==1:
                return i
        return -1


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna