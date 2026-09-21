class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        
        # 1way can be done using list

        # others by accessing element

        added_str = ''

        word1_len=len(word1)
        word2_len=len(word2)


        
        for (i,j) in zip(word1,word2):
            added_str=added_str+i+j         #abpq

            
        min_len=min(word1_len,word2_len)
        max_len = max(word1_len,word2_len)

        if word1_len!=min_len or word2_len!=min_len:
            for j in range(min_len,max_len):
                if word1_len>word2_len:
                    added_str=added_str+word1[j]
                else:
                    added_str=added_str+word2[j]


        return added_str


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna