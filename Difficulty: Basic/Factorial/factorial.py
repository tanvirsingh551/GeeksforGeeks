#User function Template for python3


class Solution:
    def factorial (self, n):
        
        # code here
        x=1
        y=1
        while x<=n:
            
            y*=x
            x+=1
        return y