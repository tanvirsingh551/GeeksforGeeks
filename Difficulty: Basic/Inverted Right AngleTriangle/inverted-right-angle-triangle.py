class Solution:
    def printPattern(self, n):
        
        #Code here
        for i in range(n):
            for j in range(i,n):
                print('*',end=' ')
            print()