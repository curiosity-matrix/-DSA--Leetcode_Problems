class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        carry=0
        # making numbers equal in length
        num1_len= len(num1)     # 3
        num2_len = len(num2)    #2
        diff=max(num1_len,num2_len)-min(num1_len,num2_len) #1
        
        if num1_len!=num2_len:
            for i in range(0,diff):
                if num1_len<num2_len:
                    num1='0'+num1  
                    num1_len+=1 
                else:
                    num2='0'+num2       #077
                    num2_len+=1

        # adding by acessing from last
        ans_sum_string=""
        for i in range (-1,-(num1_len+1),-1):
            dig_num1=ord(num1[i])-ord('0')      #6 , 5 , 4
            dig_num2=ord(num2[i])-ord('0')      #7 , 7 , 0
            summ=dig_num1+dig_num2 +carry             #13 , 12 , 4
            if len(str(summ)) == 1:
                ans_sum_string = str(summ) + ans_sum_string
                carry = 0

            else:
                ans_sum_string = str(summ)[1] + ans_sum_string
                carry = int(str(summ)[0])
                

        if carry:
            ans_sum_string=str(carry)+ans_sum_string

        return (ans_sum_string)
        

        


     

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna