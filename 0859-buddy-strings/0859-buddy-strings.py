class Solution(object):
    def buddyStrings(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        if len(s)!=len(goal):
            return(False)
        
        s_list=[]
        idx_to_swap_at=[]
        for idx,(i,j) in enumerate(zip(s,goal)):
            # since str is immutable , we need to convert it to list to swap characters
            s_list.append(i)
            if i!=j :
                idx_to_swap_at.append(idx)
        
        # swapping char in list based on idx to swap at

        if len(idx_to_swap_at)==2:
            s_list[idx_to_swap_at[0]],s_list[idx_to_swap_at[1]]=s_list[idx_to_swap_at[1]],s_list[idx_to_swap_at[0]]
        
                    # making list back to str
            s_joined=''.join(s_list)
        
            if s_joined==goal:
                return(True)
            else:
                return(False)        
        elif len(idx_to_swap_at)==0:
            for i in s:
                if s.count(i)>=2:
                    return(True)
            return (False)
        else:
            return(False)


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna