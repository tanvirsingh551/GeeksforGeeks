class Solution:
    def print_divisors(self, n):
        # code here
        for i in range(1,n+1):
            x=n%i
            if x==0:
                print(i,end=' ')
            
            