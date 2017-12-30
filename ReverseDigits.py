'''
Created on Dec 30, 2017

@author: Jake
'''
class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        ans = 0
        arr = []
        
        #if number less than ten or bigger than negative 10, return the number
        if(x < 10 and x > 0):
            return x
        elif(x > -10 and x < 0):
            return x
        
        #if x is positive, put individual numbers into array
        if(x > 0):
            while(x / 10 >= 1):
                arr.append(x % 10)
                x = int(x / 10)     
            arr.append(x)
            #add numbers in a reverse order by using factors of 10
            count = (len(arr) - 1)
            for n in (arr):
                ans += n * (10**count)
                count -= 1
        #if x is negative, remove negative, do same process as above, make negative again
        else:
            x = x * -1
            while(x / 10 >= 1):
                arr.append(x % 10)
                x = int(x / 10)     
            arr.append(x)

            count = (len(arr) - 1)
            for n in (arr):
                ans += n * (10**count)
                count -= 1
            ans = ans * -1
         
        #if answer bigger than 32 bits or, if negative, snaller than -32 bits return 0
        if(ans >= (2**31) or ans <= (-1 * (2**31))):
            return 0
        else:
            return ans